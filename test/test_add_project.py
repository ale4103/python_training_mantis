from model.project import Project
import random
import string

def test_add_project(app):
    app.session.login("administrator", "root")
    app.project.open_project_page()
    old_projects = app.project.get_project_list()
    new_project = (Project(name=random_string("Project_", 10), description=random_string("Description: ", 10)))
    app.project.create(new_project)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(new_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])