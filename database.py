from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from typing import Optional

# Создаем асинхронный движок базы данных
engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

# Создаем асинхронный фабрикатор сессий
new_session = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для моделей ORM
Base = declarative_base()

class TaskOrm(Base):  # Наследуем от Base, чтобы этот класс был привязан к таблице
    __tablename__ = "tasks"  # Определяем название таблицы

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[Optional[str]] = mapped_column()

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
 