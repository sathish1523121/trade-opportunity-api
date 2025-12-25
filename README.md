
# Trade Opportunities API

## 📌 Overview

The **Trade Opportunities API** is a FastAPI-based backend service that analyzes market data for a given business sector in India and returns a **structured market analysis report in Markdown format**.

The API is secured using an **Authorization header**, includes **rate limiting**, and exposes a **single endpoint** as required.

---

## 🚀 Features

* ✅ FastAPI backend
* ✅ Single endpoint for sector analysis
* ✅ Authorization using `Authorization` header
* ✅ Rate limiting (in-memory)
* ✅ Structured **Markdown** market analysis
* ✅ Auto-generated API documentation (Swagger UI)
* ✅ In-memory processing (no database)

---

## 🧱 Tech Stack

* **Backend Framework:** FastAPI
* **Server:** Uvicorn
* **Language:** Python
* **Authentication:** Header-based (Bearer token)
* **Storage:** In-memory (as per requirement)

---

## 📂 Project Structure

```
trade-opportunity-api/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── analyze.py
│   ├── services/
│   │   ├── search_service.py
│   │   └── ai_service.py
│   ├── security/
│   │   ├── auth.py
│   │   └── rate_limit.py
│   └── utils/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd trade-opportunity-api
```

---

### 2️⃣ Create and activate virtual environment

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the application

```bash
uvicorn app.main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## 📖 API Documentation (Swagger UI)

Swagger UI is available at:

```
http://127.0.0.1:8000/docs
```

This provides interactive API documentation and testing.

---

## 🔐 Authentication

All requests must include the following HTTP header:

```
Authorization: Bearer my-secret-key
```

Requests without this header will be rejected.

---

## 📡 API Endpoint

### Analyze Sector

```
GET /analyze/{sector}
```

### Example Request

```
GET /analyze/pharmaceuticals
```

### Headers

```
Authorization: Bearer my-secret-key
```

---

## 📤 Example Response

```json
{
  "sector": "pharmaceuticals",
  "report_markdown": "# Pharmaceuticals Sector – India\n\n## Market Overview\nRecent data indicates stable activity in the pharmaceuticals sector.\n\n## Trade Opportunities\n- Growing domestic demand\n- Export potential\n- Policy support\n\n## Risks\n- Price fluctuations\n- Regulatory uncertainty\n\n## Short-Term Outlook\nModerately positive outlook.\n"
}
```

---

## 📝 Markdown Report Format

The `report_markdown` field can be saved as a `.md` file and will render as:

```md
# Pharmaceuticals Sector – India

## Market Overview
Recent data indicates stable activity in the pharmaceuticals sector.

## Trade Opportunities
- Growing domestic demand
- Export potential
- Policy support

## Risks
- Price fluctuations
- Regulatory uncertainty

## Short-Term Outlook
Moderately positive outlook.
```

---

## 🚦 Rate Limiting

* Implemented using in-memory tracking
* Prevents excessive API usage
* Returns `429 Too Many Requests` when limit is exceeded

---

## 🧪 Testing the API (PowerShell)

```powershell
(Invoke-WebRequest http://127.0.0.1:8000/analyze/pharmaceuticals `
  -Headers @{ Authorization = "Bearer my-secret-key" } `
  -UseBasicParsing).Content
```

---

## 🎯 Purpose of the Project

This project demonstrates:

* Backend API design using FastAPI
* Secure API access
* Structured AI-style data analysis
* Clean architecture and error handling

It is suitable for **AI Engineer / Backend Engineer assignments** and technical evaluations.

---

## ✅ Status

✔ Assignment completed
✔ All requirements implemented
✔ Ready for submission

---

### ✨ Final Note

This API is designed for demonstration and evaluation purposes and uses simulated data analysis logic. It can be extended with real data sources and AI models if required.

---

