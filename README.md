# 📰 Tech News Automation

An automated system for collecting, processing, and delivering technology news via email.

This project performs web scraping on technology websites, extracts the most relevant information from articles, generates summaries using Python, and sends the results to Make through a webhook. Make orchestrates the workflow and delivers a personalized newsletter through Gmail.

## 🚀 Goal

Build an automated solution that keeps users up to date with the latest technology news without requiring them to browse multiple websites every day.

---

## ✨ Features

* Automatic news collection from technology websites, executed in parallel per source.
* Extraction of article title, content, publication date, and URL.
* Duplicate detection using normalized URLs and hashing before content extraction, avoiding unnecessary processing and repeated notifications.
* Automatic text summarization using Python.
* Webhook delivery to Make with retry and exponential backoff.
* Email newsletter distribution via Gmail.
* Isolated error handling, ensuring that failures in one source do not interrupt the entire pipeline.
* Persistent storage of processed articles and delivery status using SQLite.
* Structured logging for monitoring, debugging, and auditing.
* Modular and easily extensible architecture.

---

## 🏗️ Architecture

```text
┌──────────────────────────┐
│ Scheduler                 │
│ (Cron / GitHub Actions)   │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Scraper Manager          │
│ (parallel execution)     │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Site Extractors          │
│ TechCrunch, The Verge,   │
│ Hacker News...           │
│ → title + URL            │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Duplicate Check          │
│ (SQLite + URL hash)      │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Content Extraction       │
│ (new articles only)      │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Summarizer               │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ SQLite                   │
│ status = pending         │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Webhook Client           │
│ (retry/backoff)          │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Make Scenario            │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ Gmail                    │
└────────────┬──────────────┘
             ↓
┌──────────────────────────┐
│ SQLite                   │
│ status = sent            │
└──────────────────────────┘

        ▲
        │ Error handling & structured logging
        │ (failures are isolated and do not
        │ interrupt the entire pipeline)
```

> Duplicate checks happen **before** content extraction to avoid unnecessary processing. Articles are first persisted with `pending` status and updated to `sent` after successful webhook processing, preventing silent data loss.

---

## 🛠️ Technologies

* Python
* BeautifulSoup
* feedparser (when RSS feeds are available)
* Requests
* Sumy / NLTK (text summarization)
* SQLite (history and deduplication)
* Webhooks
* Make
* Gmail integration
* concurrent.futures (parallel execution)
* Logging module

---

## 📂 Project Structure

```text
tech-news-automation/
│
├── scraper/
│   ├── manager.py
│   ├── base_extractor.py
│   └── extractors/
│       ├── techcrunch.py
│       ├── theverge.py
│       └── hackernews.py
│
├── dedup/
│   └── history.py
│
├── summarizer/
│   ├── summarizer.py
│   └── preprocess.py
│
├── webhook/
│   └── sender.py
│
├── config/
│   └── settings.py
│
├── data/
│   └── history.db
│
├── logs/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## ⚙️ Workflow

1. The scheduler triggers the execution (Cron or GitHub Actions).
2. The Scraper Manager runs all website extractors in parallel.
3. Collected URLs are normalized and checked against the SQLite database.
4. Only new articles proceed to full content extraction.
5. The article content is summarized automatically.
6. The article is persisted with `pending` status.
7. The data is sent to the Make webhook with retries in case of failure.
8. Make processes the webhook and sends the newsletter through Gmail.
9. The article status is updated to `sent`.
10. Any errors are logged without interrupting the processing of other articles or websites.

---

## 📧 Example Email

**Subject:** Daily Technology News Digest

* 🚀 OpenAI releases a new AI model...
* 💻 GitHub announces new developer features...
* 🤖 Company X introduces an automation platform...

Read the full articles by clicking the links.

---

## 🔧 Configuration

1. Copy `.env.example` to `.env` and fill in the required variables (webhook URL, credentials, etc.).
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run locally:

```bash
python main.py
```

4. Configure the scheduler (Cron or GitHub Actions) to execute periodically.

---

## 🔮 Future Improvements

* Filter news by category (AI, Programming, Security, Cloud, etc.).
* Build a web dashboard for managing and visualizing historical data.
* Implement personalized news recommendations.
* Generate rich HTML newsletters.
* Use local or API-based LLMs for more advanced summarization.
* Add unit tests for extractors to handle website layout changes.
* Implement a direct SMTP fallback if Make becomes unavailable.
* Support HTTP caching using ETag and Last-Modified headers to reduce requests and improve efficiency.

---

## 🎯 Learning Objectives

This project was built to practice concepts such as:

* Web scraping and RSS feeds;
* Text processing and summarization;
* Deduplication and data persistence;
* Automation workflows;
* System integration using webhooks;
* Error handling and resilient pipelines;
* Modular software architecture;
* Building real-world applications with Python.
