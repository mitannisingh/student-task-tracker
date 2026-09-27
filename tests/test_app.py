from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200


def test_add_task():
    client = app.test_client()

    response = client.post(
        "/add",
        data={"title": "Test task"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test task" in response.data


def test_complete_task():
    client = app.test_client()

    client.post(
        "/add",
        data={"title": "Complete this task"}
    )

    response = client.get(
        "/complete/1",
        follow_redirects=True
    )

    assert response.status_code == 200


def test_delete_task():
    client = app.test_client()

    client.post(
        "/add",
        data={"title": "Delete this task"}
    )

    response = client.get(
        "/delete/1",
        follow_redirects=True
    )

    assert response.status_code == 200