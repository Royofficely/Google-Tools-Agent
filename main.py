import os
from dotenv import load_dotenv
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.tools import FunctionTool
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import pickle

# Load environment variables
load_dotenv()

# Set up API keys
Settings.openai_api_key = os.getenv("OPENAI_API_KEY")

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar']

def get_google_service(service_name, version):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build(service_name, version, credentials=creds)

gmail_service = get_google_service('gmail', 'v1')
calendar_service = get_google_service('calendar', 'v3')

def gmail_search(query: str) -> str:
    try:
        results = gmail_service.users().messages().list(userId='me', q=query).execute()
        messages = results.get('messages', [])
        
        if not messages:
            return "No emails found matching the query."
        
        message = gmail_service.users().messages().get(userId='me', id=messages[0]['id']).execute()
        
        headers = message['payload']['headers']
        subject = next((header['value'] for header in headers if header['name'].lower() == 'subject'), 'No subject')
        sender = next((header['value'] for header in headers if header['name'].lower() == 'from'), 'Unknown sender')
        
        snippet = message.get('snippet', 'No preview available')
        
        return f"Latest email matching the query:\nFrom: {sender}\nSubject: {subject}\nPreview: {snippet}"
    except Exception as e:
        return f"An error occurred while searching emails: {str(e)}"

def gmail_send(to: str, subject: str, body: str) -> str:
    try:
        message = create_message('me', to, subject, body)
        sent_message = gmail_service.users().messages().send(userId='me', body=message).execute()
        return f"Email sent successfully. Message ID: {sent_message['id']}"
    except Exception as e:
        return f"An error occurred while sending the email: {str(e)}"

def create_message(sender, to, subject, message_text):
    from email.mime.text import MIMEText
    import base64
    
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    return {'raw': raw_message}

def calendar_event(title: str, date: str) -> str:
    try:
        event = {
            'summary': title,
            'start': {
                'date': date,
                'timeZone': 'UTC',
            },
            'end': {
                'date': date,
                'timeZone': 'UTC',
            },
        }
        event = calendar_service.events().insert(calendarId='primary', body=event).execute()
        return f"Event created: {event.get('htmlLink')}"
    except Exception as e:
        return f"An error occurred while creating the event: {str(e)}"

def google_search(query: str) -> str:
    return f"Searching Google for: {query}"

# Create FunctionTools
gmail_search_tool = FunctionTool.from_defaults(fn=gmail_search, name="gmail_search")
gmail_send_tool = FunctionTool.from_defaults(fn=gmail_send, name="gmail_send")
calendar_tool = FunctionTool.from_defaults(fn=calendar_event, name="calendar_event")
search_tool = FunctionTool.from_defaults(fn=google_search, name="google_search")

# Combine all tools
all_tools = [gmail_search_tool, gmail_send_tool, calendar_tool, search_tool]

# Initialize the LLM
llm = OpenAI(temperature=0)

# Initialize the agent
agent = OpenAIAgent.from_tools(all_tools, llm=llm, verbose=True)

def main():
    print("Google Tools Agent initialized. You can start chatting with the agent.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting the chat. Goodbye!")
            break
        
        response = agent.chat(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    main()
