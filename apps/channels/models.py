from neattree.core.models import DefaultBaseModel


class Channel(DefaultBaseModel):

    def __str__(self):
        return '{}'.format(self.name)

