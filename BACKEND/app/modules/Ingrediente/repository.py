from sqlmodel import Session, select
from app.core.repository import BaseRepository
from app.modules.Ingrediente.models import Ingrediente

class IngredienteRepository(BaseRepository[Ingrediente]):
    
    def __init__(self, session: Session) -> None:
        """
        Inicializa el repositorio de Ingrediente.

        Args:
            session (Session): Sesión activa de base de datos.
        """
        super().__init__(session, Ingrediente)

    def get_by_nombre(self, nombre: str) -> Ingrediente | None:
        """
        Obtiene un ingrediente por su nombre.

        Args:
            nombre (str): Nombre del ingrediente.

        Returns:
            Ingrediente | None: Instancia encontrada o None si no existe.
        """
        return self.session.exec(
            select(Ingrediente).where(Ingrediente.nombre == nombre)
        ).first()

    def get_active(self, offset: int = 0, limit: int = 20) -> list[Ingrediente]:
        """
        Obtiene ingredientes con paginación.

        Args:
            offset (int): Cantidad de registros a omitir.
            limit (int): Máximo de registros a devolver.

        Returns:
            list[Ingrediente]: Lista de ingredientes.
        """
        return list(
            self.session.exec(
                select(Ingrediente)
                .offset(offset)
                .limit(limit)
            ).all()
        )

    def count_active(self) -> int:
        """
        Cuenta la cantidad total de ingredientes.

        Returns:
            int: Total de registros.
        """
        return len(
            self.session.exec(
                select(Ingrediente)
            ).all()
        )