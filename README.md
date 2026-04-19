# TaskFlow API

## 项目简介
TaskFlow API 是一个基于 Python 开发的数据驱动型 Web API，旨在帮助用户高效管理个人待办事项，并提供基于任务状态和优先级的生产力分析。

## 技术栈
- **框架**: FastAPI (Python)
- **数据库**: SQLite (SQLAlchemy ORM)
- **数据验证**: Pydantic
- **文档**: Swagger UI (OpenAPI)

## 快速开始
1. 创建并激活虚拟环境:
   `python -m venv venv`
   `source venv/bin/activate` (Linux/Mac) 或 `venv\Scripts\activate` (Windows)
2. 安装依赖:
   `pip install -r requirements.txt`
3. 运行项目:
   `uvicorn app.main:app --reload`
4. 访问接口文档:
   `http://127.0.0.1:8000/docs`

## 当前进度
- [x] 项目骨架搭建
- [x] 数据库连接配置
- [x] 核心 Task 模型定义