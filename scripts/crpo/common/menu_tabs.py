import page_elements
from logger_settings import api_logger
from scripts.crpo.common import applicant_status_change


class MenuTabs(applicant_status_change.ChangeStatus):
    def __init__(self):
        super(MenuTabs, self).__init__()

    def event_tab(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['event_tab'])
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def job_tab(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['job_tab'])
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def requirement_tab(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['requirement_tab'])
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def assessment_tab(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['assessment_tab'])
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def more_tab(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['more_tabs'])
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)

    def embrace_tab(self):
        try:
            self.x_path_element_webdriver_wait(page_elements.tabs['embrace_tab'])
            self.xpath.click()
        except Exception as error:
            api_logger.error(error)
