# CareConnect v2 – Frontend

This is the frontend for **CareConnect v2** – a chatbot interface built using Flask and Bootstrap to interact with our AI-powered mental health assistant.

## 🖼️ Overview

The frontend provides a clean, modern, mobile-friendly chat UI that interacts with the LangGraph-based backend. It handles Render cold-starts, clears chat history and delivers a realistic chat experience.

## 💡 Key Features

- Animated loading screen during backend wake-up

- Modern chat bubble layout

- Fully responsive for mobile devices

- `Clear Chat` button functionality

## 📁 Folder Structure

```
careconnect-v2-frontend/
├── templates/
│ ├── loader.html # Loader screen
│ └── chat.html # Chat UI
├── app.py # Flask backend
├── requirements.txt
└── README.md
```

## ⚙️ Setup Instructions

### 1. Clone the repo:

```bash
git clone https://github.com/shanks1554/careconnect-v2-frontend.git
cd careconnect-v2-frontend
```

### 2. Install Dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set the backend URL (edit in `app.py`)

```bash
BACKEND_URL = "your backend url"
```

### 4. Run the app:

```bash
python app.py
```

### 5. Visit:

```bash
http://127.0.0.1:5000/
```

## 🔗 Related Repo

```bash
https://github.com/shanks1554/careconnect-v2-backend.git
```