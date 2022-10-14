from typing import List
from bs4 import BeautifulSoup
from scraper.scraping import CourseScraper
from scraper.typings import Course, CourseDetails

class ARSETScraper(CourseScraper):
    
    root_url = "https://appliedsciences.nasa.gov"
    url = f"{root_url}/join-mission/training"
    courses = []
    
    def __init__(self):
        super().__init__()
        self.scrape_courses()
        
    
    def scrape_courses(self) -> None:
        self.get_courses_recursion(self.url)
        
    
    def get_courses(self) -> List[Course]:
        return self.courses
    
    
    def get_courses_recursion(self, url)-> None:
        """Get courses recursively accross the pages

        Args:
            url (str): URL of the pages of courses
        """
        
        driver = self.driver
        driver.get(url)
        
        course_page_html = driver.page_source
        course_page = BeautifulSoup(course_page_html, 'html.parser')
        
        course_list_container = course_page.find('div', attrs={'class': 'view-training'})
        
        courses_list = course_list_container.find_all('div', attrs={'class':'views-row'})
        
        for course in courses_list:
            course_categories = []
            course_image =  course.find('img').get('src')
            
            course_category_list_container = course.find('div', attrs={'class':'field--name-field-program-area'})
            
            course_category_list = course_category_list_container.find_all('div', attrs={'class':'field__item'})
            
            for category in course_category_list:
                course_categories.append(category.find('a').get_text())

            course_title = course.find('div', attrs={'class':'field--name-node-title'}).find('a').get_text()
            course_url = course.find('div', attrs={'class':'field--name-node-title'}).find('a').get('href')
            
            course_type = course.find('div', attrs={'class':'field--name-field-training-type'}).find('div', attrs={'class':'field__item'}).find('a').get_text()
            course_level = course.find('div', attrs={'class':'field--name-field-level'}).find('div', attrs={'class':'field__item'}).get_text()
            
            course_details = self.get_course_details(f'{self.root_url}{course_url}')
            
            course_dict = {
                'title':course_title, 
                'link': f'{self.root_url}{course_url}', 
                'image':f'{self.root_url}{course_image}', 
                'level':course_level, 
                'type': course_type, 
                'category':course_categories
                }
            
            course_dict.update(course_details)
            
            self.courses.append(course_dict)
        
        pagination_element = course_page.find('nav', attrs={'class':'pager'})
        
        next_element = pagination_element.find('li', attrs={'class':'pager__item pager__item--next'})
        
        if next_element:
            next_link_element = next_element.find('a').get('href')
            next_link = f'{self.url}{next_link_element}'
            self.get_courses_recursion(next_link)
        else:
            driver.close()
            return    
        
    
    
    def get_course_details(self, course_url) -> CourseDetails:
        """Get course details from its details page

        Args:
            course_url (str): Course' detail page URL

        Returns:
            CourseDetails: Dictionary value of its description and language
        """
        driver = self.driver
        driver.get(course_url)
        
        course_details_page_html = driver.page_source
        course_details_page = BeautifulSoup(course_details_page_html, 'html.parser')
        
        
        course_language = course_details_page.find('div', attrs={'class':'field--name-field-languages'}).find('div', attrs={'class':'field__item'}).find('a').get_text()
        course_description = course_details_page.find('div', attrs={'class': 'field--name-field-description'}).find('p').get_text()
        
        return {'language': course_language, 'description': course_description}
    