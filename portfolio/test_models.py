import pytest
from .factorie import ProjectFactory

@pytest.mark.django_db
def test_project_creation():
    project = ProjectFactory()
    assert project.title == 'Meu Projeto Incrível'