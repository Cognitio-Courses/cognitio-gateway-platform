from typing import List

from bs4 import BeautifulSoup, Tag
from scraper.scraping import CourseScraper


from scraper.typings import Course, CourseDetails

class EsaCourseScraper(CourseScraper):
    """ Scrapes courses data from the url property given

    """
    
    name = "ESSA"
    url = "https://eo4society.esa.int/training-education/massive-open-online-courses-moocs"
    courses = []
    
    def __init__(self):
        super().__init__()
        self.scrape_courses()
    
    
    def scrape_courses(self) -> None:
        """Scrape all courses from th url
        """
        driver = self.driver
        driver.get(self.url)
        page_html = driver.page_source
        page = BeautifulSoup(page_html, 'html.parser')
        
        
        courses_elements = page.find_all('div', attrs={"class":"single-document"})
        
        for course in courses_elements:
            course_data = self.get_course_card_details(course)
            
            self.courses.append(course_data)
        
        driver.close()
        
    
    def get_courses(self) -> List[Course]:
        """Get all courses scraped

        Returns:
            List[Course]: List of scraped courses
        """
        return self.courses
        
    
    def get_course_card_details(self, course:Tag) -> Course:
        """Get course details

        Args:
            course (Tag): Course element from BeautifulSoup

        Returns:
            Course: Dictionary of course details
        """
        thumbnail_element = course.find('div', attrs={'class': 'document-thumbnail'})
        image:str = thumbnail_element.find('a').find('img').get('src')
        link_element = course.find('div', attrs={'class':'document-title'}).find('p').find('a')
        link:str = link_element.get('href')
        title:str = link_element.get_text()
        summary:str = course.find('div', attrs={'class':'document-summary'}).find('p').get_text()
        
        course_detail = self.get_course_details(link)
        
        return Course(title=title, link=course_detail.get('link'), image=image, summary=summary, description=course_detail.get('description'))
        
    
    def get_course_details(self, url) -> CourseDetails:
        """Get course details from its details page

        Args:
            url (str): URL of the course details

        Returns:
            dict: Dictionary of course details, e.g.(Link to main course, description)
        """
        driver = self.driver
        driver.get(url)
            
        course_page = BeautifulSoup(driver.page_source,'html.parser')
        
        resource_wrapper_el = course_page.find('div', attrs={'class':'resource-wrapper'})
        
        course_link:str = resource_wrapper_el.find('div', attrs={'class':'resource-meta'}).find('a').get('href')
        description:str = resource_wrapper_el.find('div', attrs={'class':'resource-summary'}).decode_contents()
        
        
        return CourseDetails(description=description, link=course_link)
