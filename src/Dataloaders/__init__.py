from uoishelpers.dataloaders.LoaderMapBase import LoaderMapBase
from uoishelpers.dataloaders.IDLoader import IDLoader

import src.DBDefinitions
from src.DBDefinitions import BaseDBModel, EventModel, EventInvitationModel, CollectionModel, CollectionItemModel, EntityTypeModel



class LoaderMap(LoaderMapBase[BaseDBModel]):
    BaseModel = BaseDBModel

    CollectionModel: IDLoader[src.DBDefinitions.CollectionModel] = None
    CollectionItemModel: IDLoader[src.DBDefinitions.CollectionItemModel] = None
    EntityTypeModel: IDLoader[src.DBDefinitions.EntityTypeModel] = None


    EventModel: IDLoader[src.DBDefinitions.EventModel] = None
    EventInvitationModel: IDLoader[src.DBDefinitions.EventInvitationModel] = None

    def __init__(self, session):
        super().__init__(session)
        self.CollectionModel = self.get(CollectionModel)
        self.CollectionItemModel = self.get(CollectionItemModel)
        self.EntityTypeModel = self.get(EntityTypeModel)
        self.EventModel = self.get(EventModel)
        self.EventInvitationModel = self.get(EventInvitationModel)

    def get_by_name(self, name: str):
        return getattr(self, name)


def createLoadersContext(session):
    """Compatibility helper for places expecting a dict context."""
    return {'loaders': LoaderMap(session)}
