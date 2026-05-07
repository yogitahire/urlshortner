# URL Shortener

A simple URL shortener REST API built with **FastAPI**.

## Project Structure

```
urlshortner/
├── app/
│   ├── __init__.py
│   ├── main.py       # FastAPI routes
│   ├── models.py     # Pydantic request model
│   ├── store.py      # In-memory URL store
│   └── utils.py      # Short code generator
├── requirements.txt
└── README.md
```

## Setup & Run

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/shorten` | Shorten a URL |
| GET | `/{short_code}` | Redirect to original URL |
| GET | `/status/{short_code}` | Get click stats for a short URL |



Interactive docs available at: `http://localhost:8000/docs`