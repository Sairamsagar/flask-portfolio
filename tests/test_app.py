from app import app, portfolio


def test_homepage_uses_only_verified_portfolio_content():
    app.testing = True
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Sairamsagar" in response.data
    assert b"your.email@example.com" not in response.data
    assert b"your-profile" not in response.data
    assert b"Task Tracker" not in response.data
    assert b"Blog Platform" not in response.data


def test_resume_section_is_hidden_until_real_resume_is_configured():
    app.testing = True
    response = app.test_client().get("/")

    assert response.status_code == 200
    assert b"Download Resume" not in response.data
    assert b"Resume Coming Soon" not in response.data



def test_existing_configured_resume_is_linked_and_served(tmp_path, monkeypatch):
    resume = tmp_path / "resume.pdf"
    resume.write_bytes(b"resume test file")
    monkeypatch.setattr(app, "static_folder", str(tmp_path))
    monkeypatch.setitem(portfolio, "resume_filename", resume.name)

    client = app.test_client()
    page = client.get("/")
    download = client.get("/static/resume.pdf")

    assert b'href="/static/resume.pdf"' in page.data
    assert download.status_code == 200
    assert download.data == b"resume test file"


def test_project_links_render_when_configured(monkeypatch):
    project = {
        "title": "Linked Project",
        "description": "Has links.",
        "tags": [],
        "repo": "https://github.com/example/repo",
        "demo": "https://example.com/demo",
    }
    monkeypatch.setitem(portfolio, "projects", [project])

    response = app.test_client().get("/")

    assert b'href="https://github.com/example/repo"' in response.data
    assert b'href="https://example.com/demo"' in response.data
    assert b"Live demo" in response.data


def test_project_links_hidden_when_not_configured(monkeypatch):
    project = {"title": "Plain Project", "description": "No links.", "tags": []}
    monkeypatch.setitem(portfolio, "projects", [project])

    response = app.test_client().get("/")

    assert b"Plain Project" in response.data
    assert b'class="project-links"' not in response.data


def test_footer_shows_current_year():
    from datetime import date

    response = app.test_client().get("/")

    assert f"&copy; {date.today().year}".encode() in response.data


def test_debug_mode_is_disabled_by_default():
    assert app.debug is False
