import itertools
from typing import Dict, List
from bs4 import BeautifulSoup

from scraper.scraping import CourseScraper
from scraper.typings import Course


class MoocsCourseScraper(CourseScraper):
    
    root_url = "https://www.imperativemoocs.com"
    url = f"{root_url}/courses"
    name = "MOOCS"
    courses = []
   
    def __init__(self):
        super().__init__()
        self.scrape_courses()
       
    def scrape_courses(self) -> None:
        driver = self.driver
        driver.get(self.url)
        course_page_html = driver.page_source
        course_page = BeautifulSoup(course_page_html, 'html.parser')
        
        course_list_container = course_page.find('div', attrs={'class': 'w-dyn-list'})
    
        course_cards_list = course_list_container.find_all('div',attrs={'class':'courses-collection'})
        
        for course_card in course_cards_list:
            course_url = course_card.find('div', attrs={'class':'courses-content'}).find('a', attrs={'class':'courses-title'}).get('href')
            course_title = course_card.find('div', attrs={'class':'courses-content'}).find('a', attrs={'class':'courses-title'}).get_text()
            course_summary = course_card.find('div', attrs={'class':'courses-content'}).find('p').get_text()
            course_photo = course_card.find('div', attrs={'class':'courses-photo'}).find('img').get('src')
            
            course_details = self.get_course_details(f'{self.root_url}{course_url}')
            
            course = {'title': course_title, 'summary': course_summary, 'link':f'{self.root_url}{course_url}', 'photo': course_photo}
            course.update(course_details)
            self.courses.append(course)
        
        driver.close()
   
    def get_courses(self) -> List[Course]:
        
        return self.courses
    
    
    def get_course_details(self, course_url) -> Dict:
        driver = self.driver
        driver.get(course_url)
        course_page_html = driver.page_source
        course_page = BeautifulSoup(course_page_html, 'html.parser')
        
        categories = []
        
        course_page_wrapper = course_page.find('div', attrs={'class':'courses-page-wrapper'})
        course_tab_contents = course_page_wrapper.find('div', attrs={'class':'w-tab-content'}).findAll('div', recursive=False)
        
        course_description_container = course_tab_contents[0]
        
        description = course_description_container.decode_contents()
        
        course_category_container = course_page.find('div', attrs={'class':'sidebar left'}).find('div', attrs={'class':'w-dyn-items'})
        
        category_list_element = course_category_container.find_all('div', attrs={'class':'w-dyn-item'})
        
        for category_element in category_list_element:
            category = category_element.find('a').get_text()
            categories.append(category)
        
        return {'description': description, 'category': categories}