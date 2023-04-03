from datetime import datetime, timedelta
from pydantic import BaseModel


class BlizzAuthToken(BaseModel):
    access_token: str
    token_type: str
    expires_in: timedelta
    sub: str
    expires_at: datetime
