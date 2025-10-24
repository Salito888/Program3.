
from fastapi import APIRouter, HTTPException
from typing import Dict, Any
from ..service.tree_service import TreeService

router = APIRouter()
tree_service = TreeService()

@router.post("/child/", response_model=Dict[str, Any])
async def add_child(id: int, name: str, age: int):
    """
    Añade un nuevo niño al árbol.
    
    Args:
        id: Identificador único del niño
        name: Nombre del niño
        age: Edad del niño
        
    Returns:
        Diccionario con el resultado de la operación
    """
    result = tree_service.insert_child(id, name, age)
    if not result["success"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result

@router.get("/kidsbycityandgender", response_model=Dict[str, Any])
async def get_kids_by_city_and_gender():

    """
    Genera informe de cantidad de niños por ciudad y por género

    """
    return tree_service.get_kids_by_city_and_gender()
    

@router.get("/child/{child_id}", response_model=Dict[str, Any])
async def get_child(child_id: int):
    """
    Obtiene la información de un niño por su ID.
    
    Args:
        child_id: ID del niño a buscar
        
    Returns:
        Información del niño o mensaje de error
    """
    result = tree_service.find_child(child_id)
    if not result["success"]:
        raise HTTPException(status_code=404, detail=result["message"])
    return result

@router.get("/tree/", response_model=Dict[str, Any])
async def get_tree():
    """
    Obtiene la representación completa del árbol.
    
    Returns:
        Estructura completa del árbol y su estado de balance
    """
    return tree_service.get_tree()

@router.get("/tree/balance/", response_model=Dict[str, Any])
async def check_balance():
    """
    Verifica si el árbol está balanceado.
    
    Returns:
        Estado de balance del árbol
    """
    return tree_service.check_balance()

@router.delete("/tree/", response_model=Dict[str, Any])
async def clear_tree():
    """
    Elimina todos los nodos del árbol.
    
    Returns:
        Resultado de la operación
    """
    return tree_service.clear_tree()
    