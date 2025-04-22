from fastapi import APIRouter, HTTPException, UploadFile, Form
from backend.services.summarizer_service import summarize_paper
from backend.api.schemas.summarization import SummarizationRequest, SummarizationResponse

router = APIRouter()

@router.post("/", response_model=SummarizationResponse)
async def summarize(file: UploadFile, summary_length: str = Form("medium")):
    try:
        content = await file.read()
        text = content.decode("utf-8")
        summary = summarize_paper(text, summary_length)
        return SummarizationResponse(summary=summary)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
