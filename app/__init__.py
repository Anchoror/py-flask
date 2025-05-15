from tkinter import SW
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # 初始化数据库
    db.init_app(app)
    migrate.init_app(app, db)

    # 注册蓝图
    from .routes import main

    app.register_blueprint(main)

    # 注册错误处理器
    from .errors import register_error_handlers

    register_error_handlers(app)

    # 配置日志
    from .logger import setup_logger

    setup_logger(app)

    # 配置 Swagger UI
    SWAGGER_URL = "/api/docs"
    API_URL = "/static/swagger.json"

    # 注册 Swagger UI 蓝图
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Flask API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
