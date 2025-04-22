from fastapi import APIRouter, HTTPException, UploadFile, Form
from backend.services.citation_service import find_citations
from backend.api.schemas.citation_finder import CitationRequest, CitationResponse

router = APIRouter()

@router.post("/", response_model=CitationResponse)
async def find_related_citations(file: UploadFile, num_results: int = Form(5)):
    try:
        content = await file.read()
        text = content.decode("utf-8")
        citations = find_citations(text, num_results)
        return CitationResponse(citations=citations)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
