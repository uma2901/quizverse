# QuizVerse — Django Quiz Application

A multi-category quiz app. Enter your name, pick a topic, answer a set of
multiple-choice questions, and see your score with a full answer review.
Every attempt is saved to the database and shown on a leaderboard.

## Features
- Multiple quiz categories (General Knowledge, Aptitude, Reasoning — 30 questions included)
- One-page quiz form with instant grading on submit
- Full answer review after submission (shows correct answer + your answer for each question)
- Leaderboard showing the top 10 scores across all attempts, stored in the database
- Django Admin panel to add/edit categories, questions, and view all attempts
- Clean, responsive UI

## 1. Setup

```bash
python3 -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Set up the database

```bash
python manage.py migrate
```

## 3. Load the demo questions

```bash
python manage.py seed_questions
```

You should see:
```
Created category: General Knowledge
Created category: Aptitude
Created category: Reasoning
Done. 3 categories and 30 questions ready.
```

## 4. Run the app

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

## 5. (Optional) Add your own questions via Django Admin

```bash
python manage.py createsuperuser
```
Then log in at **http://127.0.0.1:8000/admin/**.

## Project structure

```
quiz_project/
├── manage.py
├── requirements.txt
├── quiz_project/            # project settings/urls
└── quiz_app/                 # the actual app
    ├── models.py              # Category, Question, QuizAttempt
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── management/commands/seed_questions.py
    ├── templates/quiz_app/
    └── static/quiz_app/style.css
```

## Talking points for your presentation

- **MVT architecture**: three models (Category, Question, QuizAttempt) working together.
- **Session usage**: player name and category carried via Django sessions.
- **Full CRUD in the Admin panel**: add/edit/delete questions and categories, review attempts.
- **Aggregation/ordering**: leaderboard uses `.order_by('-score')`.
