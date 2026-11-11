from pathlib import Path

from flask import Flask, render_template, url_for

app = Flask(__name__)

portfolio = {
    "name": "Sairamsagar",
    "headline": "Flask and Python portfolio project.",
    "bio": "This portfolio is a work in progress. More information will be added soon.",
    "github": "https://github.com/Sairamsagar",
    "resume_filename": None,
    "projects": [
        {
            "title": "Flask Portfolio",
            "description": "A responsive single-page portfolio built with Flask, Jinja2, HTML, and CSS.",
            "tags": ["Flask", "Python", "HTML", "CSS"],
        },
    ],
}


@app.route('/')
def home():
    resume_filename = portfolio.get('resume_filename')
    resume_path = Path(app.static_folder) / resume_filename if resume_filename else None
    resume_url = (
        url_for('static', filename=resume_filename)
        if resume_path and resume_path.is_file()
        else None
    )
    return render_template(
        'portfolio.html',
        portfolio=portfolio,
        resume_url=resume_url,
    )


if __name__ == '__main__':
    app.run(debug=False)
