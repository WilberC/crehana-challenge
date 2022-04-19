from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class CrehanaBaseSchema(BaseModel):
    id: Optional[int]
    # Todo add timestamps to models could be useful for audit
    # created_at: Optional[datetime]
    # updated_at: Optional[datetime]
