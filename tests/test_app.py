import pytest

from app import app, portfolio


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_homepage_renders_portfolio_content(client):
    response = client.get("/")

    assert response.status_code == 200
    assert portfolio["name"].encode() in response.data
    assert portfolio["projects"][0]["title"].encode() in response.data


def test_resume_section_is_hidden_without_a_resume_file(client):
    assert b"Download Resume" not in client.get("/").data


def test_resume_is_linked_and_served_when_configured(client, tmp_path, monkeypatch):
    (tmp_path / "resume.pdf").write_bytes(b"resume test file")
    monkeypatch.setattr(app, "static_folder", str(tmp_path))
    monkeypatch.setitem(portfolio, "resume_filename", "resume.pdf")

    assert b'href="/static/resume.pdf"' in client.get("/").data
    assert client.get("/static/resume.pdf").data == b"resume test file"


def test_unknown_path_returns_404_page(client):
    response = client.get("/missing-page")

    assert response.status_code == 404
    assert b"Page not found" in response.data


def test_health_check(client):
    response = client.get("/healthz")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_security_headers_are_set(client):
    for path in ("/", "/missing-page"):
        headers = client.get(path).headers

        assert headers["X-Content-Type-Options"] == "nosniff"
        assert headers["X-Frame-Options"] == "DENY"
        assert "script-src 'none'" in headers["Content-Security-Policy"]
