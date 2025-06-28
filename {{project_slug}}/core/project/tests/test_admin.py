import httpx


def test_ping_endpoint():
    """Test ping endpoint returns correct response."""
    with httpx.Client(base_url="http://localhost:8000") as client:
        response = client.get("/admin/login/?next=/admin")

        assert response.status_code == 200
