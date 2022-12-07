def test_vowel_count(flask_client):
    payload = {"words": ["batman", "robin", "coringa"]}
    r = flask_client.post("/api/vowel_count", json=payload)

    assert r.status_code == 200
    assert r.json == {"batman": 2, "robin": 2, "coringa": 3}


def test_vowel_count_without_params_return_bad_request(flask_client):
    r = flask_client.post("/api/vowel_count")

    assert r.status_code == 400


def test_vowel_count_error_get(flask_client):
    r = flask_client.get("/api/vowel_count")
    assert r.status_code == 405
