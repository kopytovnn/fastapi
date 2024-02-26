from datetime import datetime
from enum import Enum

from pydantic import BaseModel, HttpUrl

class Body(BaseModel):
    action: list
    release: list