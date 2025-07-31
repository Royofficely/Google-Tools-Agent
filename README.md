# 🤖 Google Tools Agent

An intelligent agent that seamlessly interacts with Google services, including Gmail and Calendar, while also simulating Google searches. Powered by OpenAI's language models for natural language processing and task automation.

## ✨ Features

- 📧 **Gmail Integration** – Search, read, and send emails with natural language commands
- 📅 **Calendar Management** – View, create, and manage Google Calendar events
- 🔍 **Google Search Simulation** – Intelligent search functionality with AI-powered results
- 🧠 **AI-Powered Interactions** – Natural conversation interface using OpenAI's language models
- 🔒 **Secure Authentication** – OAuth 2.0 integration with Google services
- 💬 **Interactive Chat Interface** – Easy-to-use command-line interface
- 🚀 **One-Command Setup** – Automated configuration and authentication process

## 🛠️ Prerequisites

- **Python 3.7+**
- **Google Cloud Console account**
- **OpenAI API key** ([Get one here](https://platform.openai.com/api-keys))
- **Internet connection** (for API calls and authentication)

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone https://github.com/yourusername/google-tools-agent.git
cd google-tools-agent
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Google Credentials

#### Step-by-Step Google Cloud Setup

1. **Create Google Cloud Project**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project or select existing one
   - Note your project ID for reference

2. **Enable Required APIs**
   - Navigate to "APIs & Services" → "Library"
   - Search and enable these APIs:
     - ✅ **Gmail API**
     - ✅ **Google Calendar API**

3. **Create OAuth 2.0 Credentials**
   ```
   APIs & Services → Credentials → Create Credentials → OAuth client ID
   ```
   - **Application Type**: Desktop application
   - **Name**: Google Tools Agent (or your preferred name)
   - Click "Create"

4. **Download Credentials**
   - Download the JSON file from the credentials page
   - Rename it to `credentials.json`
   - Place it in your project root directory

### 5. Initialize and Authenticate

```bash
python agentim.py setup
```

This command will:
- 🔑 Prompt for your OpenAI API key
- 🌐 Open browser for Google OAuth authentication
- 💾 Save authentication tokens securely

### 6. Run the Agent

```bash
python agentim.py run
```

## 💬 Usage Examples

Once running, try these natural language commands:

### Email Operations
```
"Check my recent emails"
"Send an email to john@example.com about the meeting tomorrow"
"Search for emails from my boss last week"
"Show me unread emails"
```

### Calendar Management
```
"What's on my calendar today?"
"Schedule a meeting with Sarah for next Tuesday at 2 PM"
"Show me my events for this week"
"Cancel my 3 PM appointment"
```

### Search Functionality
```
"Search for Python tutorials"
"Find information about machine learning"
"Look up the weather forecast"
```

### Exit the Agent
```
exit
quit
bye
```

## ⚙️ Configuration

### Environment Variables

The setup process creates a `.env` file with:

```env
OPENAI_API_KEY=your_openai_api_key_here
GOOGLE_CREDENTIALS_PATH=credentials.json
```

### Advanced Configuration

You can customize the agent's behavior by modifying configuration variables in `agentim.py`:

```python
# Model selection
MODEL = "gpt-3.5-turbo"  # or "gpt-4"

# Response settings
MAX_TOKENS = 150
TEMPERATURE = 0.7
```

## 🔒 Security & Privacy

- **OAuth 2.0**: Secure authentication with Google services
- **Local Storage**: Tokens stored locally in `token.pickle`
- **API Keys**: Stored securely in `.env` file
- **No Data Collection**: Your data stays between you, Google, and OpenAI

### Important Security Notes

- Never commit `credentials.json` or `.env` to version control
- Keep your API keys confidential
- Review permissions during OAuth flow
- Regularly rotate API keys for production use

## 🔧 Troubleshooting

### Common Issues

**Authentication Problems**
```bash
# Clear existing tokens and re-authenticate
rm token.pickle
python agentim.py setup
```

**Missing Credentials**
```bash
# Verify credentials file exists
ls -la credentials.json

# Check file contents (should be val
