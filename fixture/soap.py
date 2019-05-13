from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_from_soap(self):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        test = client.service.mc_projects_get_user_accessible('administrator', 'root')
        list = []
        for i in test:
            id = i.id
            name = i.name
            description = i.description
            project_list = Project(id=id, name=name, description=description)
            list.append(project_list)
        return list