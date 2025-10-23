
from fastapi import FastAPI
from app.ABB.controller.tree_controller import router as tree_router

app = FastAPI(title="API de Árbol Binario de Búsqueda")

app.include_router(tree_router, prefix="/api/v1", tags=["ABB"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

