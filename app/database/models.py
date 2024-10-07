import os

from tortoise import Tortoise, fields, models
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()


async def init_db():
    await Tortoise.init(
        db_url=os.getenv('DATABASE_URL'),
        modules={"models": ["app.database.models"]}
    )
    await Tortoise.generate_schemas()


class User(models.Model):
    id = fields.IntField(primary_key=True)
    telegram_id = fields.BigIntField(unique=True)
    daily_tasks: fields.ReverseRelation["DailyTask"]
    custom_tasks: fields.ReverseRelation["CustomTask"]
    created_at = fields.DatetimeField(default=datetime.utcnow)
    updated_at = fields.DatetimeField(default=datetime.utcnow)

    class Meta:
        table = "users"


class DailyTask(models.Model):
    id = fields.IntField(primary_key=True)
    user = fields.ForeignKeyField("models.User", related_name="daily_tasks", on_delete=fields.CASCADE)
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    completed = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(default=datetime.utcnow)
    updated_at = fields.DatetimeField(default=datetime.utcnow)

    class Meta:
        table = "daily_tasks"


class CustomTask(models.Model):
    id = fields.IntField(primary_key=True)
    every_day = fields.BooleanField(default=False)
    user = fields.ForeignKeyField("models.User", related_name="custom_tasks", on_delete=fields.CASCADE)
    title = fields.CharField(max_length=255)
    description = fields.TextField(null=True)
    completed = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(default=datetime.utcnow)
    updated_at = fields.DatetimeField(default=datetime.utcnow)

    class Meta:
        table = "custom_tasks"
