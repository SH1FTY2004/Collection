from sqlalchemy import ForeignKey
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.DBDefinitions.BaseModel import BaseDBModel, IDType


__all__ = [
    "EntityTypeModel",
]


class EntityTypeModel(BaseDBModel):
    """Číselník typů entit, které lze vložit do kolekce (strom typů)."""
    __tablename__ = "entity_types"


    name: Mapped[Optional[str]] = mapped_column(nullable=True, default=None, comment="např. Projekt, Dokument",)
