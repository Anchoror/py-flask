from pickle import FALSE


class Config:
    DEBUG = False
    TESTING = FALSE
    SECRET_KEY = ""
    JWT_SECRET_KEY = "your-secret-key"
    JWT_ACCESS_TOKEN_EXPIRES = 3600


class DevelopmentConfig(Config):
    DEBUG = True  # 开发环境开启调试模式
    SQLALCHEMY_DATABASE_URI = "sqlite:///dev.db"  # 开发数据库


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # 从环境变量获取数据库连接
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")  # 从环境变量获取 JWT 密钥
    LOG_LEVEL = logging.INFO


config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig,
}
