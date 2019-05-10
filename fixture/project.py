from model.project import Project
import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.20/manage_proj_page.php")

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def edit_project_field_value(self, field_name, text):
        if text is not None:
            wd = self.app.wd
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_project_form(self, project):
        wd = self.app.wd
        self.edit_project_field_value("name", project.name)
        self.edit_project_field_value("description", project.description)

    def create(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('input[value="Create New Project"]').click()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[value='Add Project']").click()
        time.sleep(5)

    def select_project_by_index(self, index):
        wd = self.app.wd
        print("index = ", index)
        project = wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:][index]
        project.find_element_by_xpath("./td[1]/a").click()

    def delete_project(self, name):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_xpath("//a[contains(text(), '%s')]" % name).click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()
        wd.find_element_by_css_selector('input[value="Delete Project"]').click()


    def get_project_list(self):
        wd = self.app.wd
        self.open_project_page()
        project_list = []
        for element in wd.find_elements_by_xpath('//table[@class="width100"]//tr[@class="row-1"]'):
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            id = (element.find_element_by_css_selector('a').get_attribute('href')).split('=')[1]
            project_list.append(Project(id=id, name=name, description=description))

        for element in wd.find_elements_by_xpath('//table[@class="width100"]//tr[@class="row-2"]'):
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            id = (element.find_element_by_css_selector('a').get_attribute('href')).split('=')[1]
            project_list.append(Project(id=id, name=name, description=description))
        return project_list