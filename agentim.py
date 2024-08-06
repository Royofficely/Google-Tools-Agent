import os
import sys
import subprocess
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.send', 'https://www.googleapis.com/auth/calendar']

def install_dependencies():
    """Install the required dependencies using pip within the virtual environment."""
    pip_path = os.path.join('venv', 'bin', 'pip') if os.name != 'nt' else os.path.join('venv', 'Scripts', 'pip.exe')
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])
    print("Dependencies installed successfully.")

def setup_google_credentials():
    """Setup or refresh Google credentials."""
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
        print("Google authentication completed successfully.")
    else:
        print("Google credentials are valid.")

def setup():
    """Run the setup for environment and Google credentials."""
    print("Setting up environment variables and Google credentials...")
    if not os.path.exists(".env"):
        openai_api_key = input("Enter your OpenAI API key: ")
        with open(".env", "w") as f:
            f.write(f"OPENAI_API_KEY={openai_api_key}\n")
        print(".env file created and updated successfully with API keys.")
    else:
        print(".env file already exists. Please update it manually if needed.")
    setup_google_credentials()

def install():
    print("Installing dependencies and setting up the virtual environment...")
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', 'venv'])
    install_dependencies()

def run():
    print("Running Google Tools Agent...")
    python_path = os.path.join('venv', 'bin', 'python') if os.name != 'nt' else os.path.join('venv', 'Scripts', 'python.exe')
    subprocess.check_call([python_path, 'main.py'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python agentim.py [install|run|setup]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "install":
        install()
    elif command == "run":
        run()
    elif command == "setup":
        setup()
    else:
        print(f"Unknown command: {command}")
        print("Usage: python agentim.py [install|run|setup]")
        sys.exit(1)
