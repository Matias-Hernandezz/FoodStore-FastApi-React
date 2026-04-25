from sqlmodel import Session
from app.core.unit_of_work import UnitOfWork
from app.modules.Producto.repository import ProductoRepository
# Importamos repositorios de otros módulos para validaciones cruzadas
from app.modules.Categoria.repository import CategoriaRepository
from app.modules.Ingrediente.repository import IngredienteRepository

class ProductoUnitOfWork(UnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.productos = ProductoRepository(session)
        self.categorias = CategoriaRepository(session)
        self.ingredientes = IngredienteRepository(session)