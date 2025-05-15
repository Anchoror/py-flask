import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger(app):
    """配置日志系统"""
    # 创建日志目录（如果不存在）
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # 设置日志级别
    app.logger.setLevel(logging.INFO)

    # 定义日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    # 文件处理器（按大小轮转）
    file_handler = RotatingFileHandler(
        "logs/app.log", maxBytes=1024 * 1024 * 10, backupCount=10
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # 添加处理器到应用日志
    if not app.logger.handlers:
        app.logger.addHandler(file_handler)
        app.logger.addHandler(console_handler)

    # 记录启动信息
    app.logger.info("Application started")
