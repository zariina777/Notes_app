from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.notes import NoteCreate, NoteUpdate
from ..crud.notes import (
    get_notes,
    get_note_by_id,
    create_note_in_db,
    update_note_in_db,
    delete_note_in_db,
    restore_note_in_db,
    search_note_in_db,
    get_notes_pagination,
    archive_note_in_db
)
async def fetch_notes(db: AsyncSession, show_deleted: bool = False, category: Optional[str] = None):
    return await get_notes(db, show_deleted=show_deleted, category=category)
async def create_note_service(db: AsyncSession, note: NoteCreate):
    note_data = note.dict()
    return await create_note_in_db(db, note_data)
async def update_note_service(db: AsyncSession, note_id: int, note_update: NoteUpdate):
    db_note = await get_note_by_id(db, note_id)
    if not db_note:
        return None
    update_data = note_update.dict(exclude_unset=True)
    return await update_note_in_db(db, db_note, update_data)
async def delete_note_service(db: AsyncSession, note_id: int):
    db_note = await get_note_by_id(db, note_id)
    if not db_note:
        return None
    return await delete_note_in_db(db, db_note)
async def restore_note_service(db: AsyncSession, note_id: int):
    db_note = await get_note_by_id(db, note_id)
    if not db_note:
        return None
    return await restore_note_in_db(db, db_note)

async def search_note_service(db: AsyncSession, query: str):
    return await search_note_in_db(db, query=query)

async def get_notes_service(db: AsyncSession, limit: int, offset: int):
    return await get_notes_pagination(db, limit=limit, offset=offset)

async def archive_note_service(db: AsyncSession, note_id: int):
    db_note = await get_note_by_id(db, note_id)
    if not db_note:
        return None
    return await archive_note_in_db(db, db_note)

async def active_note_service(db: AsyncSession, note_id: int):
    db_note = await get_note_by_id(db, note_id)
    if not db_note:
        return None
    return await active_note_service(db, db_note)