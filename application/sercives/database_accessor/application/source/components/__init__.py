from application.sercives.database_accessor.application.configurations import (
    configuration,
)

from ...models import Relation
from ..configurations import ids
from .functionalities import Functionalities
from .relations import Relations

relation = Relation(configuration=configuration)


class Objects:

    @property
    def relations(self):

        return Relations()

    @property
    def functionalities(self):

        return Functionalities()


objects = Objects()
