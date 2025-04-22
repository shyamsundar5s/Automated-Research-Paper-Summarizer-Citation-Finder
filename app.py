from fastapi import FastAPI
from backend.api.routes import summarization, citation_finder, health_check

app = FastAPI(
    title="Research Paper Summarizer and Citation Finder",
    description="A tool to summarize research papers and find related citations.",
    version="1.0.0"
)

# Include API routes
app.include_router(summarization.router, prefix="/api/summarization", tags=["Summarization"])
app.include_router(citation_finder.router, prefix="/api/citation", tags=["Citation Finder"])
app.include_router(health_check.router, prefix="/api/health", tags=["Health Check"])
