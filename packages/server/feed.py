from pydantic import BaseModel


class CreateFeedRequest(BaseModel):
    feed_url: str
