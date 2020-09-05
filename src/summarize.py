from summarizer import Summarizer
from src.store import save_summary


def summarize_text(text: str, document_id: int) -> None:
    """Summarize the given text and save it into the database."""
    model = Summarizer()
    summary_list = model(
        text,
        
        # minimum/maximum of characters per sentence in the given text
        min_length=4,
        max_length=4_000
    )
    summary = ''.join(summary_list)

    save_summary(summary, document_id)