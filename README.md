# 🧪 RUT Validator API

A simple FastAPI-based service to validate Chilean RUT (Rol Único Tributario). Useful for businesses, HR departments, and developers working with Chilean identity data.

## 🚀 Features

- Validates RUT format and check digit
- Simple JSON API
- Ready to deploy with Docker

## 📦 Installation (Without Docker)

1. Clone the repo:

```bash
git clone https://github.com/yourusername/rut-validador.git
cd rut-validador/backend
```

2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the server:

```bash
uvicorn main:app --reload
```

## 🐳 Running with Docker

1. Build the image:

```bash
docker build -t rut-validador .
```

2. Run the container:

```bash
docker run -d -p 8000:8000 rut-validador
```

3. Access the API at:

```
http://localhost:8000/docs
```

## 📫 Endpoint

**POST** `/validate_rut/`

### Request Body:
```json
{
  "rut": "12345678K"
}
```

### Response:
```json
{
  "valid": true
}
```

## 🛠 Technologies

- FastAPI
- Python 3.10+
- Docker

## 📄 License

MIT - Free for personal and commercial use.
