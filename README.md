
# BERT-based Django Sentiment Analysis App

This project is a BERT-based Django App for performing sentiment analysis on news articles. The system fetches news from an external API, processes it using a sentiment analysis model, and stores the results in a database.

---

## Features

- **REST API Endpoint**: Provides an API for executing sentiment analysis.
- **Authentication**: Uses Django REST Framework’s **Token Authentication** for secure access.
- **Sentiment Analysis**: Utilizes `ProsusAI/finbert` via Hugging Face Transformers to analyze sentiment.
- **News API Integration**: Fetches news articles dynamically from an external news API.
- **Database Storage**: Stores processed news articles along with their sentiment scores.
- **Automatic Token Creation**: Uses Django signals to create an authentication token when a new user is registered.

---

## Requirements

- Python 3.x
- Django
- Django REST Framework
- Django Token Authentication
- Django CORS Handling
- PyTorch
- Hugging Face `transformers`
- Requests

---

## Installation

1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Set up environment variables in a .env file.
6. Create a superuser.

   ```bash
   python manage.py createsuperuser
   ```

---

## API Usage

### **Authentication & Token Generation**

This API uses **Token Authentication**. Upon user creation, a **token is automatically generated** using Django signals (`signals.py`).

To obtain or use the token:

```bash
curl -H "Authorization: Token your_token_here" http://127.0.0.1:8000/test/
```

### **Trigger Sentiment Analysis**

- **Endpoint**: `GET /test/`
- **Description**: Fetches news articles, runs sentiment analysis, and stores the results.

---

## Sentiment Analysis Logic

- **Model Used**: `ProsusAI/finbert` (a financial sentiment analysis model).
- **Pipeline**: Sentiment scores and labels (e.g., positive, neutral, negative) are generated using a transformer-based model.
- **Storage**: The processed results are stored in the `sentiment_results` database table.

Example Sentiment Calculation:

```python
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="ProsusAI/finbert")
result = sentiment_pipeline("Stock prices are falling rapidly.")[0]

print(result)
# Output: {'label': 'negative', 'score': 0.98}
```

---

## URL Configuration

The API URLs are defined in `urls.py`. The endpoint for executing sentiment analysis is:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^test/', views.execute_API.as_view())
]
```

- `/test/` → Calls `execute_API` to fetch news, analyze sentiment, and store results.

---

## Licensing

- **News API**: Ensure compliance with the terms of the external news API you use.
- **Sentiment Analysis Model**: `ProsusAI/finbert` is available via [Hugging Face](https://huggingface.co/ProsusAI/finbert).

---

