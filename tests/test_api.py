from fastapi.testclient import TestClient
import pytest

import sys; sys.path.append("..")
from config import settings
from main import app
from scripts.create_database import create_table
from src.store import get_database_cursor


settings.database_file = ":memory:"
client = TestClient(app)

example_text = (
    'Squirrels are often the cause of power outages. They can readily climb a power pole and crawl or run along a power cable. '
    'The animals will climb onto power transformers or capacitors looking for food, or a place to cache acorns. If they touch a '
    'high voltage conductor and a grounded portion of the enclosure at the same time, they are electrocuted, and often cause a '
    'short circuit that shuts down equipment. Squirrels have brought down the high-tech NASDAQ stock market twice and were '
    'responsible for a spate of power outages at the University of Alabama. To sharpen their teeth, squirrels will often chew on '
    'tree branches or even the occasional live power line. Rubber or plastic plates, or freely rotating sleeves ("squirrel guards") '
    'are sometimes used to discourage access to these facilities.'
)


@pytest.fixture
def database_session():
    session = get_database_cursor()
    yield session
    session.connection.close()


@pytest.fixture
def setup_database(database_session, monkeypatch):
    # don't close (and thus remove) the in-memory test database
    monkeypatch.setattr("src.store.get_database_cursor", lambda: database_session.connection.cursor())
    monkeypatch.setattr("src.store.commit_and_close", lambda session: session.connection.commit())

    create_table(database_session)


@pytest.mark.usefixtures("setup_database")
def test_create_summary():
    # create summary
    response = client.post("/summaries/",
                          data={"text": example_text})
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["document_id"] == 1


    # get summary
    response = client.get("/summaries/1")
    assert response.status_code == 200, response.text

    data = response.json()
    assert data["document_id"] == 1
    assert data["summary"] == (
        "Squirrels are often the cause of power outages. If they touch a high voltage conductor and a grounded portion of the enclosure at "
        "the same time, they are electrocuted, and often cause a short circuit that shuts down equipment."
    )
