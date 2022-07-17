from fastapi import FastAPI, APIRouter
from views import author_router, assets_router
import uvicorn

app = FastAPI()
router = APIRouter()


@router.get('/')
def first():
    return "Helo World"


app.include_router(prefix='/first', router=router)
app.include_router(author_router)
app.include_router(assets_router)

if __name__ == '__main__':
    uvicorn.run('main:app', port=8081, reload=True, host='0.0.0.0')
