from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional, List

# 基础模型，包含共有的验证逻辑
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="任务标题不能为空")
    description: Optional[str] = Field(None, max_length=500)
    status: str = Field("pending", pattern="^(pending|in_progress|completed)$", description="状态必须是 pending, in_progress 或 completed")
    priority: str = Field("medium", pattern="^(low|medium|high)$", description="优先级必须是 low, medium 或 high")
    due_date: Optional[datetime] = None

# 创建任务时的请求体
class TaskCreate(TaskBase):
    pass

# 更新任务时的请求体 (所有字段可选)
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1)
    description: Optional[str] = None
    status: Optional[str] = Field(None, pattern="^(pending|in_progress|completed)$")
    priority: Optional[str] = Field(None, pattern="^(low|medium|high)$")
    due_date: Optional[datetime] = None

# 统一响应格式
class TaskResponse(TaskBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True # 允许兼容 SQLAlchemy 模型