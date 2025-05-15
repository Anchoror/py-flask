import json

def test_get_users(client, test_user):
    """测试获取用户列表"""
    response = client.get("/api/users")
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]["username"] == "test"

def test_create_user(client):
    """测试创建用户"""
    data = {
        "username": "new_user",
        "email": "new@example.com",
        "password": "test123"
    }
    
    response = client.post(
        "/api/users",
        json=data,
        content_type="application/json"
    )
    
    assert response.status_code == 201
    assert json.loads(response.data)["username"] == "new_user"    