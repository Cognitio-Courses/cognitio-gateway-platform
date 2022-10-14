from typing import List
from bs4 import BeautifulSoup
from scraper.scraping import CourseScraper
from scraper.typings import Course, CourseDetails


class EOCollegeScraper(CourseScraper):
    url = "https://eo-college.org/courses/"
    name = "eo-college"
    courses = []
    
    def __init__(self):
        super().__init__()
        self.scrape_courses()
    
    def scrape_courses(self) -> None:
        """Scrape courses from its URL given
        """
        driver = self.driver
        driver.get(self.url)
        
        course_page_html = driver.page_source
        course_page = BeautifulSoup(course_page_html, 'html.parser')
        courses_container = course_page.find('div', attrs={'class':'ld-course-list-items'})
        
        courses_list = courses_container.find_all('div', attrs={'class': 'ld_course_grid'})
        
        for course in courses_list:
            course_cover = course.find('div', attrs={'class': 'bb-course-cover'})
            course_image = course_cover.find('img').get('src')
            
            course_details = course.find('div', attrs={'class', 'bb-card-course-details'})
            
            course_title = course_details.find('h2', attrs={'class': 'bb-course-title'}).find('a').get_text()
            course_url = course_details.find('h2', attrs={'class': 'bb-course-title'}).find('a').get('href')
            try:
                course_summary = course_details.find('div', attrs={'class': 'entry-content'}).get_text()
            except:
                course_summary = ""
            
            course_description = self.get_course_details(course_url)
            
            self.courses.append({'title':course_title, 'image': course_image, 'summary': course_summary, 'link':course_url, 'description': course_description.get('description')})
        
        driver.close()
    
    def get_courses(self) -> List[Course]:
        """Get courses scraped

        Returns:
            List[Course]: List of courses scraped
        """
        return self.courses
    
    def get_course_details(self, course_url) -> CourseDetails:
        """Course details from its detail page

        Args:
            course_url (str): URL of the course

        Returns:
            CourseDetails: Course details containg dictionary of descrription
        """
        driver = self.driver
        driver.get(course_url)
        
        course_page_html = driver.page_source
        course_page = BeautifulSoup(course_page_html, 'html.parser')
        
        
        course_description = course_page.find('div', attrs={'class': 'ld-tabs-content'}).find('div', attrs={'aria-labelledby':'content'}).decode_contents()
        
        return {'description': course_description}
        
        
        
    