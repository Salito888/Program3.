
from typing import Dict, List, Optional, Any
from model.tree_model import ABB, Child, NodoABB
from collections import defaultdict


class TreeService:
    """
    Servicio para manejar las operaciones del Árbol Binario de Búsqueda (ABB).
    """
    def __init__(self):
        self.tree = ABB()
    
    def insert_child(self, id: int, name: str, age: int, city: str, gender: str) -> Dict[str, Any]:
        """
        Inserta un nuevo niño en el árbol.
        
        Args:
            id: Identificador único del niño
            name: Nombre del niño
            age: Edad del niño
            
        Returns:
            Diccionario con el resultado de la operación
        """
        try:
            # Verificar si ya existe un niño con esa identificación
            if self.tree.find_by_id(id) is not None:
                return {
                    "success": False,
                    "message": f"Ya existe un niño con la identificación {id}"
                }
            
            # Crear y agregar el nuevo niño
            new_child = Child((101, "María García", 7, "Cali", "Female"), 
            (70, "Juan Pérez", 6, "Manizales", "Male"),
            (6, "Ana López", 8, "Manizales", "Female"),
            (-2, "Carlos Sánchez", 7, "Cali", "Male"),
            (100, "Laura Torres", 9, "Medellín", "Female"),
            (90, "Pedro Ramírez", 6, "Bogotá", "Male"),
            (30, "Sofía Díaz", 8, "Pereira", "Female"),
            (46, "Diego Castro", 7, "Pereira", "Male"),
            (99, "Elena Ruiz", 9, "Pereira", "Female"),
            (33, "Miguel Ángel Soto", 8, "Manizales", "Male"))
            self.tree.insert(new_child)
            
            return {
                "success": True,
                "message": "Niño agregado correctamente",
                "child": new_child.to_dict(),
                "is_balanced": self.tree.is_balanced()
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al insertar el niño: {str(e)}"
            }
    
    def find_child(self, id: int) -> Dict[str, Any]:
        """
        Busca un niño por su identificación.
        
        Args:
            id: Identificador del niño a buscar
            
        Returns:
            Diccionario con el resultado de la búsqueda
        """
        try:
            child = self.tree.find_by_id(id)
            
            if child is None:
                return {
                    "success": False,
                    "message": f"No se encontró ningún niño con la identificación {id}"
                }
                
            return {
                "success": True,
                "child": child.to_dict()
            }
            
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al buscar el niño: {str(e)}"
            }

    
    
    def get_tree(self) -> Dict[str, Any]:
        """
        Obtiene la representación completa del árbol.
        
        Returns:
            Diccionario con la estructura del árbol y su estado de balance
        """
        try:
            return {
                "success": True,
                "tree": self.tree.to_dict(),
                "is_balanced": self.tree.is_balanced()
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al obtener el árbol: {str(e)}"
            }
    
    def check_balance(self) -> Dict[str, Any]:
        """
        Verifica si el árbol está balanceado.
        
        Returns:
            Diccionario con el estado de balance del árbol
        """
        try:
            is_balanced = self.tree.is_balanced()
            return {
                "success": True,
                "is_balanced": is_balanced,
                "message": "El árbol está balanceado" if is_balanced else "El árbol NO está balanceado"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al verificar el balance: {str(e)}"
            }
    
    def clear_tree(self) -> Dict[str, Any]:
        """
        Limpia el árbol, eliminando todos los nodos.
        
        Returns:
            Diccionario con el resultado de la operación
        """
        try:
            self.tree.clear()
            return {
                "success": True,
                "message": "Árbol limpiado correctamente"
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"Error al limpiar el árbol: {str(e)}"
            }


    def get_kids_by_city_and_gender(self) -> Dict[str, Any]:
      """
      Genera un informe de cantidad de niños por ciudad y género.
      """
    try:
        data = defaultdict(lambda: {"female": 0, "male": 0})

        def traverse(node: Optional[NodoABB]):
            if node:
                child = node.child
                if child.city and child.gender:
                    gender = child.gender.lower()
                    if gender in ("female", "male"):
                        data[child.city][gender] += 1
                traverse(node.left)
                traverse(node.right)

        traverse(self.tree.root)

        # Tabla de reportes
        report = []
        for city, counts in data.items():
            total_city = counts["female"] + counts["male"]
            report.append({
                "City": city,
                "Gender": {
                    "female": counts["female"],
                    "male": counts["male"]
                },
                "Cant": total_city
            })

        # Totales generales
        total_female = sum(c["Gender"]["female"] for c in report)
        total_male = sum(c["Gender"]["male"] for c in report)
        total = total_female + total_male
        
        return {
            "success": True,
            "Report": report,
            "Totals": {
                "female": total_female,
                "male": total_male,
                "total": total
            }
        }
        except Exception as e:
            return {
            "success": False,
            "message": f"Error al generar el informe: {str(e)}"
        }

            