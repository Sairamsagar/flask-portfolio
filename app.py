from flask import Flask, render_template, url_for

app = Flask(__name__)

portfolio = {
    "name": "Your Name",
    "headline": "Building clean web experiences with Python and Flask.",
    "bio": (
        "I am a developer who loves turning ideas into polished, responsive websites. "
        "I focus on readable code, user-friendly interfaces, and projects that scale."
    ),
    "email": "your.email@example.com",
    "linkedin": "https://www.linkedin.com/in/your-profile",
    "resume_filename": "your-resume.pdf",
    "projects": [
        {
            "title": "Portfolio Website",
            "description": "A modern portfolio built with Flask, templating, and responsive styling.",
            "tags": ["Flask", "HTML", "CSS"],
        },
        {
            "title": "Task Tracker",
            "description": "A lightweight task manager with clean UI and productive workflows.",
            "tags": ["Python", "Web App", "UX"],
        },
        {
            "title": "Blog Platform",
            "description": "A blog template that supports reusable content sections and easy updates.",
            "tags": ["Flask", "Markdown", "Content"],
        },
    ],
}


@app.route('/')
def home():
    return render_template(
        'portfolio.html',
        portfolio=portfolio,
        resume_url=url_for('static', filename=portfolio['resume_filename']),
    )


if __name__ == '__main__':
    app.run(debug=True)
