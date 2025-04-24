# AI News to Social Media Bot  
*AI-Powered Social Media Content Generator*

## 🧠 Project Overview

**Purpose:**  
This project fetches AI-related news articles, summarizes them, and automatically posts them to social media platforms (Twitter, LinkedIn, Instagram) using pre-built APIs.

**Workflow:**
1. Fetch AI news from an online source (**NewsAPI**).
2. Summarize the content using a local LLaMA model (**llama 3.1**).
3. Generate social media posts tailored for Twitter (optionally LinkedIn and Instagram).
4. Post to social media using platform APIs.

---

## ⚙️ Project Setup & Running Instructions

### ✅ Requirements
- Python 3.7 or higher

### 📦 Required Libraries
- `streamlit`
- `requests`
- `json`
- `llama` (for LLaMA model inference)
- `instagrapi` (optional, for Instagram posting)

> Note: Twitter and LinkedIn API keys are required. You must create developer accounts for each platform.

### 🪛 Step-by-Step Guide

#### 1. Install Required Libraries
Run the following to install dependencies:

```bash
pip install -r requirements.txt
```

#### 2. Get API Keys

- **Twitter:**  
  Create a developer account and get:  
  `Consumer Key`, `Consumer Secret`, `Access Token`, `Access Token Secret`

- **LinkedIn:**  
  Create a LinkedIn Developer Application and obtain:  
  `Client ID`, `Client Secret`

- **Instagram (optional):**  
  Use the `instagrapi` library. You may need an active Instagram account.

#### 3. Configuration

Create a file named `config.py` to securely store your API keys.

#### 4. Run the Application

Use the following command inside your project directory:

```bash
streamlit run <file_name>.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

#### 5. Using the App

Click the **"Fetch & Post News"** button to:
- Fetch the latest AI news.
- Summarize the articles.
- Generate and post them on social media.

---

## 🧩 Script Descriptions

### `1. fetch_news.py` — *Trending News Fetching*
- **Purpose:** Get latest AI news articles from NewsAPI.
- **Function:** Makes HTTP requests and returns article lists.

### `2. summarize.py` — *Content Generation*
- **Purpose:** Summarize articles using LLaMA model.
- **Function:** Sends article text to the LLaMA API and gets summaries.

### `3. generate_post.py` — *Post Formatting & Media*
- **Purpose:** Create platform-ready social media posts.
- **Function:** Formats summaries and URLs for Twitter, LinkedIn, and Instagram.

### `4. post.py` — *Posting*
- **Purpose:** Post content to selected social media accounts.
- **Function:** Uses API keys to authenticate and post content.

### `5. main1.py` — *Orchestrator Script*
- **Purpose:** Integrates all components into a full workflow.
- **Function:** Handles fetching, summarizing, formatting, posting, and saving outputs.

### `6. dashboard.py` — *Streamlit Dashboard*
- **Purpose:** Provides a UI to control the workflow manually.
- **Functionality:**
  - Buttons to trigger each step.
  - Displays success messages.
  - Optional Instagram/LinkedIn integration (commented out).
  - Uses `st.balloons()` for feedback.
  - Perfect for non-technical users or demos.

---

## 💾 Stored Output Files

- `fetched_news`: Raw AI news articles from NewsAPI.
- `summarized_news`: Summaries (with titles and URLs) in JSON format.
- `latest_post`: The final generated post before posting to Twitter.