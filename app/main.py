from fastapi import FastAPI
from .database import engine, Base

# 初始化数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskFlow API",
    description="一个用于个人任务管理与效率分析的 Web API",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"message": "欢迎使用 TaskFlow API! 访问 /docs 查看文档。"}