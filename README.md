# Smart Lab Helper

Smart Lab Helper is a Flask-based web app that helps learners practice Python labs, submit solutions, and get instant feedback.  
It also comes with an AI Assistant powered by a Hugging Face model for quick hints and explanations.

---

## Features
- **Lab List** – Choose from multiple Python labs.
- **Lab Instructions** – View detailed steps for each lab.
- **Submission Check** – Submit your code and get instant feedback.
- **AI Assistant** – Ask lab-related questions and get AI-powered answers.

---

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap
- **AI Model**: `distilgpt2` (Hugging Face Transformers)
- **Others**: Torch, JSON APIs

---

## 📂 Project Structure
```
project/  
│   
├── app.py # Main Flask app   
├── utils/   
│ └── check_submission.py # Submission checking logic
├── templates/
│ ├── index.html
│ ├── labs.html
│ ├── lab_detail.html
│ └── feedback.html
├── labs/ # Markdown files with lab instructions
│ ├── lab1.md
│ ├── lab2.md
│ └── ...
└── static/
└── style.css
```
---

## ⚙️ Installation & Run
1. **Install Dependencies**  
`pip install flask transformers torch`

2. **Run the App**   
`python app.py` 

3.**Usage**   
Visit `http://127.0.0.1:5000`   

---
## 📜 **License**  
MIT License © 2025

