from app import create_app


def test_home_route():
    app = create_app()
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_component_route_not_found():
    app = create_app()
    client = app.test_client()
    response = client.get("/components/does-not-exist")
    assert response.status_code == 404
