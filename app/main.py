from fastapi import FastAPI
from app.api.v1.notes import router as notes_router
from app.core.init_db import init_db

app = FastAPI()



@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(notes_router, prefix="/apy/v1/notes" , tags=["notes"])