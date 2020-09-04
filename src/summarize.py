from summarizer import Summarizer
from src.store import save_summary


def summarize_text(long_text: str, document_id: int) -> None:
    """Summarize the given text and save it into the database."""
    model = Summarizer()
    summary_list = model(long_text)
    summary = ''.join(summary_list)
    save_summary(summary, document_id)
