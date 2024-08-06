import sys
import subprocess
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar']

def install():
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    create_env_file()
    check_google_credentials()
    print("Dependencies installed successfully.")
    print("Please run 'python agentim.py setup' to configure API keys and Google authentication.")

def run():
    print("Running Google Tools Agent...")
    subprocess.check_call([sys.executable, "main.py"])

def create_requirements():
    requirements = [
        "python-dotenv",
        "llama-index",
        "openai",
        "google-auth-oauthlib",
        "google-auth-httplib2",
        "google-api-python-client"
    ]
    with open("requirements.txt", "w") as f:
        for req in requirements:
            f.write(f"{req}\n")
    print("requirements.txt file created.")

def create_env_file():
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("OPENAI_API_KEY=\n")
        print(".env file created with empty placeholders for API keys.")
    else:
        print(".env file already exists. Skipping creation.")

def setup_env_file():
    openai_api_key = input("Enter your OpenAI API key: ")

    with open(".env", "w") as f:
        f.write(f"OPENAI_API_KEY={openai_api_key}\n")

    print(".env file updated successfully with API keys.")

def check_google_credentials():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists("credentials.json"):
                print("Google credentials file (credentials.json) not found.")
                print("Please follow these steps to set up your Google credentials:")
                print("1. Go to the Google Cloud Console (https://console.cloud.google.com/)")
                print("2. Create a new project or select an existing one")
                print("3. Enable the Gmail API and Google Calendar API for your project")
                print("4. Create credentials (OAuth 2.0 Client ID) for a desktop application")
                print("5. Download the credentials JSON file")
                print("6. Rename the downloaded file to 'credentials.json'")
                print("7. Place 'credentials.json' in the project root directory")
                input("Press Enter when you have completed these steps...")
            
            if os.path.exists("credentials.json"):
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)
                print("Google authentication completed successfully.")
            else:
                print("credentials.json file still not found. Please make sure to follow the steps above.")
                return
    else:
        print("Google credentials are valid.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agentim.py [install|run|setup]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "install":
        create_requirements()
        install()
    elif command == "run":
        run()
    elif command == "setup":
        setup_env_file()
        check_google_credentials()
    else:
        print(f"Unknown command: {command}")
        print("Usage: python agentim.py [install|run|setup]")
        sys.exit(1)
