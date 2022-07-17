from fastapi import APIRouter, HTTPException, status
from schemas import AuthorCreateInput, StandardOutput, ErrorOutput
from services import AuthorService

author_router = APIRouter(prefix='/author')
assets_router = APIRouter(prefix='/assets')


@author_router.post('/create',
                    description='Adicione novos autores ao banco de dados',
                    response_model=StandardOutput,
                    responses={400: {'model': ErrorOutput}}
                    )
async def author_create(author_input: AuthorCreateInput):
    try:
        await AuthorService.create_author(
            name=author_input.name,
            username=author_input.username,
            picture=author_input.picture,
            country=author_input.country,
            bio=author_input.bio
        )
        return StandardOutput(message='Tudo certo!')
    except Exception as error:
        raise HTTPException(400, detail=str(error))

#Deletar Autor
@author_router.delete('/delete/{author_id}',
                      description='Remova autores do banco de dados',
                      response_model=StandardOutput,
                      responses={400: {'model': ErrorOutput}}
                      )
async def author_create(author_id: int):
    try:
        await AuthorService.delete_author(author_id)
        return StandardOutput(message='Autor deletado do banco de dados')
    except Exception as error:
        raise HTTPException(400, detail=str(error))


