# Flask Portfolio

A responsive portfolio site built with Flask, Jinja, HTML, and CSS. The current page contains only verified project details; add personal contact information and a resume when you are ready.

---

## Features

- **Single-page layout** — About, Projects, and Contact sections; the resume section appears only when a configured PDF exists
- **Responsive design** — Mobile-first CSS Grid and Flexbox, works on all screen sizes
- **Template-driven** — Easy to customize via the `portfolio` dictionary in `app.py`
- **Automated tests** — Run locally with pytest; GitHub Actions checks pushes and pull requests
- **Zero JavaScript dependencies** — Pure HTML/CSS, fast loads
- **Modern styling** — CSS custom properties, fluid typography, subtle shadows

---

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (included with Python)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Sairamsagar/flask-portfolio.git
cd flask-portfolio

# 2. Create a virtual environment
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

## Project Structure

```
flask-portfolio/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── requirements-dev.txt   # Test dependency
├── Procfile               # Production server command
├── tests/                  # Application tests
├── .github/workflows/      # GitHub Actions CI
├── README.md             # This file
├── LICENSE               # MIT License
├── .gitignore            # Git ignore rules
├── static/
│   ├── style.css         # All styling
│   └── (add a real resume PDF here, if desired)
└── templates/
    └── portfolio.html    # Jinja2 template
```

---

## Customization

Edit `app.py` to personalize your portfolio. The `portfolio` dictionary holds all the content:

```python
portfolio = {
    "name": "Your Name",
    "headline": "Your tagline here",
    "bio": "Your bio/description...",
    "github": "https://github.com/Sairamsagar",
    "resume_filename": None,  # Set only when a real PDF exists in static/
    "projects": [
        {
            "title": "Project Name",
            "description": "What it does...",
            "tags": ["Tech", "Stack", "Here"],
            "repo": "https://github.com/...",  # Optional: shows a "Code" link
            "demo": None,  # Optional: shows a "Live demo" link
        },
        # Add more projects...
    ],
}
```

### Add your resume

1. Place your PDF in `static/` (for example, `static/john-doe-resume.pdf`).
2. Update `resume_filename` in `app.py` to match the filename.

### Styling

Modify `static/style.css`. CSS custom properties at the top of the file make theme changes straightforward:

```css
:root {
    --accent: #14532d;      /* Primary brand color */
    --bg: #eff4fb;          /* Page background */
    --surface: #ffffff;     /* Card backgrounds */
    /* ... */
}
```

---

## Development

### Run locally

Debug mode is disabled by default. For local development, use Flask's debug mode explicitly only on your own machine. Install the development dependency and run the test suite with:

```bash
python app.py
pip install -r requirements-dev.txt
python -m pytest -q
```

### Linting (optional)

```bash
pip install ruff
ruff check .
ruff format .
```

---

## Deployment

The `Procfile` starts Gunicorn and binds to the host-provided `PORT`. Use a Linux-based Python host that supports Gunicorn. The Flask development server is not for production. No environment variables or application secrets are currently required; `.env.example` records that status.

### Option 1: Gunicorn + Nginx (Production VPS)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Configure Nginx to proxy requests to `localhost:8000`.

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

- **Render**, **Fly.io**, or **Railway** — push to GitHub, connect the repo, and enable auto-deploy
- **PythonAnywhere** — upload the files and configure the WSGI settings
- **Heroku** — add a `Procfile` with `web: gunicorn app:app`

---

## Contributing

### Branches

| Branch | Purpose | How it changes |
|---|---|---|
| `main` | Production. Always working and deployable. Clone this to run the site. | Only by a release pull request from `develop` |
| `develop` | Integration. The next release is assembled and tested here. | Only by squash-merged pull requests from work branches |
| `feat/...`, `fix/...`, `docs/...`, `chore/...` | One change each, branched from `develop` | Deleted after merge |

Nobody pushes to `main` or `develop` directly. Both require a pull request with the `test` check passing.

### Making a change

```bash
git clone https://github.com/Sairamsagar/flask-portfolio.git
cd flask-portfolio
git switch develop
git switch -c feat/short-description

python -m pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q

git push -u origin feat/short-description
```

Then open a pull request **into `develop`** and squash-merge it once the check passes.

### Releasing to production

1. Open a pull request from `develop` into `main`.
2. Merge it with a merge commit (not squash), so the two branches keep a shared history.
3. Tag the result on `main`, for example `v1.1.0`, and publish a GitHub release.

For an urgent production fix, branch `fix/...` from `main`, open the pull request into `main`, then merge `main` back into `develop`.

---

## License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) — lightweight WSGI framework
- CSS custom properties for straightforward theming
