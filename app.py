from datetime import date
from pathlib import Path

from flask import Flask, jsonify, render_template, url_for

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
            "repo": "https://github.com/Sairamsagar/flask-portfolio",
            "demo": None,
        },
    ],
}


SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "strict-origin-when-cross-origin",
    "Permissions-Policy": "camera=(), geolocation=(), microphone=()",
    # The page loads one same-origin stylesheet, no scripts, and an inline SVG favicon.
    "Content-Security-Policy": (
        "default-src 'self'; "
        "img-src 'self' data:; "
        "script-src 'none'; "
        "object-src 'none'; "
        "base-uri 'self'; "
        "form-action 'none'; "
        "frame-ancestors 'none'"
    ),
}


@app.after_request
def add_security_headers(response):
    for header, value in SECURITY_HEADERS.items():
        response.headers.setdefault(header, value)
    return response


@app.route('/healthz')
def healthz():
    return jsonify(status="ok")


@app.errorhandler(404)
def page_not_found(error):
    return (
        render_template(
            '404.html',
            portfolio=portfolio,
            current_year=date.today().year,
        ),
        404,
    )


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
        current_year=date.today().year,
    )


if __name__ == '__main__':
    app.run(debug=False)
