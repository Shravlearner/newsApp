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
- ✅ Apply filters: date range, source name, language (The language filter is yet to be implmented as the NewsApi everything/ endpoint which we're using doesn't yet have a parameter for languages)
- ✅ Restricting access to blocked users by admin

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
cd newsApp
```

### 2. Create Virtual environment

```bash
python -m venv env # (You may use the virtual environment module as well using pip install virtualenv)
On Windows: env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r ../requirements.txt
```
### 4. Migrate Database
```bash
python manage.py migrate
```
### 5. Creat super user(for admin access)
```bash
python manage.py createsuperuser
```
### 6. Run the server
```bash
python manage.py runserver
```
Open your browser and go to: http://127.0.0.1:8000
👤 Admin Panel
Visit: http://127.0.0.1:8000/admin

Log in with your superuser credentials

Manage users, searches, and block/unblock users

🔐 Authentication Features
Only authenticated users can search and view results

Inactive/blocked users cannot log in

Custom friendly message for blocked users 

Each user can only see their own search history and results

📄 Functional Highlights
🔁 Prevent Repetitive API Calls
If a user searches the same keyword within 15 minutes:

A message is shown and saved results are used.

🔄 Refresh Results
Clicking “Refresh” on results page:

Only fetches newer articles than the most recent saved one.

🔍 Filters
You can filter search results by:

✅ Date range (start/end)

✅ Source name (e.g., BBC, CNN)

✅ Language (e.g., en, hi) (limited support due to NewsAPI restrictions)

✍️ How Django Is Used
Models: Search, Article connected via foreign key

Views: Handle user actions, API integration, DB interaction

Templates: Render HTML using Django Template Language

Admin: User and model management

Middleware: Used for custom login messaging

💡 Future Enhancements (Bonus Ideas)
✅ Show original news article in a modal (same page)

⏰ Background job to auto-refresh tracked searches

📊 Admin dashboard showing trending keywords

🔢 Quota per user on tracked keywords

📌 Requirements
See requirements.txt for all Python dependencies.


