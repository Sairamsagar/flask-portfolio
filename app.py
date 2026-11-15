from datetime import date
from pathlib import Path

from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)

# All page content lives here. Edit this dictionary to personalise the site.
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
    # The site loads one same-origin stylesheet, no scripts, and an inline SVG favicon.
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


@app.context_processor
def inject_site_context():
    """Make the portfolio content and the current year available to every template."""
    return {"portfolio": portfolio, "current_year": date.today().year}


@app.after_request
def add_security_headers(response):
    for header, value in SECURITY_HEADERS.items():
        response.headers.setdefault(header, value)
    return response


def get_resume_url():
    """Return the URL of the configured resume, or None when the file does not exist."""
    filename = portfolio.get("resume_filename")
    if filename and (Path(app.static_folder) / filename).is_file():
        return url_for("static", filename=filename)
    return None


@app.route("/")
def home():
    return render_template("portfolio.html", resume_url=get_resume_url())


@app.route("/healthz")
def healthz():
    return jsonify(status="ok")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=False)
