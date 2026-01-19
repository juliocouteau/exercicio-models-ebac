import factory
from .models import Project

class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    title = 'Meu Projeto Incrível'
    description = 'Descrição do projeto'
    technology = 'Django'