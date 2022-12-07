import pytest

from backend import create_app


@pytest.fixture
def app():
    client = create_app()
    client.config.update(
        {
            "TESTING": True,
        }
    )

    yield client


@pytest.fixture
def flask_client(app):
    return app.test_client()
