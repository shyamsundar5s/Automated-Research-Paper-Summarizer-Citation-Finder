from pydantic import BaseModel

class SummarizationRequest(BaseModel):
    paper_content: str
    summary_length: str

class SummarizationResponse(BaseModel):
    summary: str
