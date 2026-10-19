import typing
import datetime
from typing import Optional
import dataclasses
import sqlalchemy
from sqlalchemy import (
    Column,
    String,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import Mapped, mapped_column, synonym

from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, column_property

from src.DBDefinitions.BaseModel import BaseDBModel, UUIDColumn, UUIDFKey, IDType

###########################################################################################################################
#
# zde definujte sve SQLAlchemy modely
# je-li treba, muzete definovat modely obsahujici jen id polozku, na ktere se budete odkazovat
#
###########################################################################################################################
class CollectionItemModel(BaseDBModel):
    __tablename__ = "collection_items" 

    collection_id: Mapped[typing.Optional[IDType]] = mapped_column(ForeignKey("collections.id"), default=None, nullable=True, comment="Event assigned to the invitation")
    user_id: Mapped[Optional[IDType]] = UUIDFKey(ForeignKey("users.id"), default=None, nullable=True, comment="User assigned to the invitation")
    entity_id: Mapped[IDType] = mapped_column(default=None, nullable=True)
    entity_type_id: Mapped[Optional[IDType]] = mapped_column(ForeignKey("entitytypes.id"), index=True, nullable=True, default=None,)
    #entity_type = 
    position: Mapped[int] = mapped_column(default=None, nullable=True)


   