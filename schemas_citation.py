from pydantic import BaseModel
from typing import List, Dict

class CitationRequest(BaseModel):
    paper_content: str
    num_results: int

class CitationResponse(BaseModel):
    citations: List[Dict[str, str]]
