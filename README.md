# Flask Portfolio

A clean, responsive personal portfolio website built with **Flask**, **Jinja2 templates**, and modern **CSS**. Designed for developers who want a lightweight, customizable portfolio without heavy frameworks.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## ✨ Features

- **Single-page layout** — About, Projects, Resume, Contact sections
- **Responsive design** — Mobile-first CSS Grid/Flexbox, works on all screens
- **Template-driven** — Easy to customize via `app.py` data dictionary
- **Resume download** — Place your PDF in `static/` and link works automatically
- **Zero JS dependencies** — Pure HTML/CSS, fast loads
- **Modern styling** — CSS custom properties, fluid typography, subtle shadows

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (comes with Python)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/flask-portfolio.git
cd flask-portfolio

# 2. Create a virtual environment (recommended)
python -m venv venv

# 3. Activate the environment
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Windows (cmd):
.\venv\Scripts\activate.bat
# macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the development server
python app.py
```

Open your browser at **http://127.0.0.1:5000/**

---

## 📁 Project Structure

```
flask-portfolio/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── LICENSE               # MIT License
├── .gitignore            # Git ignore rules
├── static/
│   ├── style.css         # All styling
│   └── your-resume.pdf   # Place your resume here (optional)
└── templates/
    └── portfolio.html    # Jinja2 template
```

---

## ✏️ Customization

Edit `app.py` to personalize your portfolio:

```python
portfolio = {
    "name": "Your Name",
    "headline": "Your tagline here",
    "bio": "Your bio/description...",
    "email": "you@example.com",
    "linkedin": "https://linkedin.com/in/yourprofile",
    "resume_filename": "your-resume.pdf",  # Must match file in static/
    "projects": [
        {
            "title": "Project Name",
            "description": "What it does...",
            "tags": ["Tech", "Stack", "Here"]
        },
        # Add more projects...
    ],
}
```

### Add your resume
1. Place your PDF in `static/` (e.g., `static/john-doe-resume.pdf`)
2. Update `resume_filename` in `app.py` to match

### Styling
Modify `static/style.css` — CSS custom properties at the top make theme changes trivial:
```css
:root {
    --accent: #14532d;      /* Primary brand color */
    --bg: #eff4fb;          /* Page background */
    --surface: #ffffff;     /* Card backgrounds */
    /* ... */
}
```

---

## 🛠️ Development

### Run with auto-reload (debug mode)
```bash
python app.py
```
The app runs with `debug=True` — changes to Python/templates auto-reload.

### Linting (optional)
```bash
pip install ruff
ruff check .
ruff format .
```

---

## 📦 Deployment

### Option 1: Gunicorn + Nginx (Production VPS)
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
Configure Nginx to proxy to `localhost:8000`.

### Option 2: Docker
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```
```bash
docker build -t flask-portfolio .
docker run -p 5000:5000 flask-portfolio
```

### Option 3: Platform-as-a-Service
- **Render** / **Fly.io** / **Railway** — Push to GitHub, connect repo, auto-deploy
- **PythonAnywhere** — Upload files, configure WSGI
- **Heroku** — Add `Procfile`: `web: gunicorn app:app`

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) — Lightweight WSGI framework
- [Inter font](https://fonts.google.com/specimen/Inter) — Clean, readable typography
- CSS custom properties for effortless theming

---

> **Tip:** Star ⭐ this repo if you found it useful!
