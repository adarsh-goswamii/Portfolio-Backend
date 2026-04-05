from pydantic import BaseModel


class ResumeActiveOut(BaseModel):
    s3_url: str
    version_label: str
