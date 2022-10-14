from bs4 import BeautifulSoup, Tag
from scraper.scraping import CourseScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EumetSatScraper(CourseScraper):
    
    root_url: str = "https://trainingevents.eumetsat.int"
    name: str = "eumet"
    url: str = "https://trainingevents.eumetsat.int/trui/"
    
    def get_courses(self):
        
        driver = self.driver
        driver.get(self.url)
        
        while True:
            try:
                event_list = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'event-list'))
                )
                break
            except Exception as e:
                print(e)
                continue
        
        course_page_html = driver.page_source
        course_page = BeautifulSoup(course_page_html, 'html.parser')
        
        course_list_container = course_page.find('div', attrs={'id':'event-list'})
        
        courses_container = course_list_container.find_all('div', attrs={'class':'card'})
        
        for course in courses_container:
            course = self.get_course_details(course)
            self.courses.append(course)
            print(course)

        return self.courses
    
    
    def get_course_details(self, course:Tag):
        course_card_header = course.find('div', attrs={'class':'card-header'})
        course_title = course_card_header.find('div').find('a').find('strong').get_text()
        
        course_card_body = course.find('div', attrs={'class':'card-body'})
        course_type = course_card_body.find('div', attrs={'class':'card-title'}).find('strong').get_text()
        course_summary = course_card_body.find('p', attrs={'class':'card-text'})
        
        return {'title': course_title, 'summary': course_summary, 'type': course_type}