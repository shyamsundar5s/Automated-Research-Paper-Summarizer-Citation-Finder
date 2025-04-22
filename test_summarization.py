from backend.services.summarizer_service import summarize_paper

def test_summarize_paper():
    content = "This is a test content. It is meant to test the summarization functionality."
    summary = summarize_paper(content, "short")
    assert isinstance(summary, str)
    assert len(summary) > 0
