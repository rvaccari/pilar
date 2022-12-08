def test_sort_asc(flask_client):
    payload = {"words": ["batman", "robin", "coringa"], "order": "asc"}
    r = flask_client.post("/api/sort", json=payload)

    assert r.status_code == 200
    assert r.json == ["batman", "coringa", "robin"]


def test_sort_desc(flask_client):
    payload = {"words": ["batman", "robin", "coringa"], "order": "desc"}
    r = flask_client.post("/api/sort", json=payload)

    assert r.status_code == 200
    assert r.json == ["robin", "coringa", "batman"]
