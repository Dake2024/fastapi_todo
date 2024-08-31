from pydantic import BaseModel

class STaskAdd(BaseModel):
    name: str
    description: str | None = None  # Устанавливаем значение по умолчанию

class STask(STaskAdd):
    id: int

    class Config:
        from_attributes = True  # Включаем поддержку from_orm

class STaskId(BaseModel):
    ok: bool = True
    task_id: int