from transformers import pipeline

# Initialize summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_paper(content: str, length: str) -> str:
    length_map = {"short": 50, "medium": 100, "detailed": 200}
    max_length = length_map.get(length, 100)  # Default to medium
    summary = summarizer(content, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
