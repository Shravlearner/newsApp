# 📰 News Tracker App (Django)

This is a Django-based web application that allows registered users to search for news articles on any topic, filter them based on various criteria, and view recent headlines. It also supports user management (including blocking/unblocking users) via the admin panel.

---

## 🚀 Features

- ✅ User authentication (register, login, logout)
- ✅ Search for real-time news articles using **NewsAPI**
- ✅ View your search history
- ✅ Auto-refresh news articles for a query without duplicating existing ones
- ✅ Prevent repeated searches within a 15-minute window
- ✅ Admin dashboard to **block/unblock users**
- ✅ Display of latest headlines on the homepage
- ✅ Sort articles by publish date (newest/oldest)
- ✅ Apply filters: date range, source name, language
- ✅ Friendly message for blocked/inactive users

---

## 📦 Tech Stack

- Python 3.10
- Django 5.x
- SQLite (default DB)
- NewsAPI (https://newsapi.org)
- Bootstrap 5 for UI

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/shravlearner/newsApp.git
cd newsApp/src

### 2. Create Virtual environment

