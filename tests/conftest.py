import pytest
from app import create_app, db
from app.models.user import User

@pytest.fixture
def app():
    """创建测试应用实例"""
    app = create_app("testing")  # 使用测试配置
    app.config["TESTING"] = True
    
    with app.app_context():
        db.create_all()  # 创建测试数据库
        yield app        # 提供应用实例给测试函数
        db.drop_all()    # 清理测试数据库

@pytest.fixture
def client(app):
    """创建测试客户端"""
    return app.test_client()

@pytest.fixture
def test_user(app):
    """创建测试用户"""
    with app.app_context():
        user = User(username="test", email="test@example.com", password_hash="test")
        db.session.add(user)
        db.session.commit()
        return user