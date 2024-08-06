# 🤖 Google Tools Agent

An intelligent agent that seamlessly interacts with Google services, including Gmail and Calendar, while also simulating Google searches.

## 🌟 Features

- 📧 Gmail integration (search and send emails)
- 📅 Google Calendar management
- 🔍 Simulated Google Search functionality
- 🧠 AI-powered interactions using OpenAI's language model

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/google-tools-agent.git
cd google-tools-agent
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Configure Google Credentials 🔑

Follow these steps to create your `credentials.json` file:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the following APIs for your project:
   - Gmail API
   - Google Calendar API

   To enable these APIs:
   - In the Cloud Console, go to "APIs & Services" > "Library"
   - Search for each API and click on it
   - Click the "Enable" button

4. Create OAuth 2.0 credentials:
   - Go to "APIs & Services" > "Credentials"
   - Click "Create Credentials" > "OAuth client ID"
   - Select "Desktop app" as the application type
   - Give your OAuth client a name (e.g., "Google Tools Agent")
   - Click "Create"

5. Download the credentials:
   - After creating the OAuth client, you'll see a modal with your client ID and client secret
   - Click the download button (download icon) to download the JSON file
   - Rename the downloaded file to `credentials.json`
   - Move `credentials.json` to your project's root directory

### 4. Install Dependencies 📦

```bash
python agentim.py install
```

### 5. Set Up API Keys and Authentication 🔐

```bash
python agentim.py setup
```

This command will:
- Prompt you to enter your OpenAI API key
- Initiate the Google OAuth flow for authentication

### 6. Run the Agent 🚀

```bash
python agentim.py run
```

## 💬 Usage

Once the agent is running, interact with it by typing commands or questions. The agent can perform various tasks related to Gmail, Google Calendar, and simulated Google Search.

To exit the agent, simply type 'exit'.

## 📝 Notes

- 🌐 During the initial setup or first run, a browser window will open for Google OAuth authentication. Follow the prompts to grant the necessary permissions.
- 🔒 Ensure that your `credentials.json` and `.env` files are kept secure and not shared publicly.
- ⚠️ This setup is suitable for personal use and testing. If you plan to distribute this application or use it in a production environment, you'll need to go through additional steps, including verifying your app with Google and setting up the OAuth consent screen.

## 🛠️ Troubleshooting

If you encounter issues with Google authentication:

1. Verify that `credentials.json` is present in the project root directory
2. Remove the `token.pickle` file (if it exists) and run `python agentim.py setup` again
3. Confirm that you've enabled the required APIs (Gmail and Calendar) in your Google Cloud Console project

For any other issues, please open an issue on the GitHub repository.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/google-tools-agent/issues).

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- OpenAI for their powerful language models
- Google for their comprehensive API services

---

Made with ❤️ by [Your Name]
