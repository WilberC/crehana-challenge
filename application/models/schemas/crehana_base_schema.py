from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CrehanaBaseSchema(BaseModel):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
