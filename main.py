from fastapi import BackgroundTasks, FastAPI, Form
from src.store import create_summary_id, get_summary
from src.summarize import summarize_text_and_save_to_database

app = FastAPI()


@app.get("/summaries/{document_id}")
async def read_summary(document_id: int):
    """Get the summary for the given ID."""
    return {
        "document_id": document_id,
        "summary": get_summary(document_id),
    }


@app.post("/summaries/")
async def create_summary(background_tasks: BackgroundTasks, text: str = Form(...)):
    """Summarize the given text and return the ID under which the summary will be stored."""
    document_id = create_summary_id()

    # summarize the long text using a background task since this takes some time to finish
    background_tasks.add_task(summarize_text_and_save_to_database, text, document_id)

    return {"document_id": document_id}
