from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy import delete
from database.models import Author
from database.connection import async_session


class AuthorService:
    async def create_author(name, username, picture, country, bio):
        async with async_session() as session:
            session.add(Author(
                name=name,
                username=username,
                picture=picture,
                country=country,
                bio=bio)
            )
            await session.commit()

    async def delete_author(author_id):
        async with async_session() as session:
            await session.execute(delete(Author).where(Author.id == author_id))
            await session.commit()


