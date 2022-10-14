from typing import List
from scraper.driver import Driver
import json
from time import time
import os

from scraper.typings import Course


class CourseScraper:
    """Course scaper base class.
    Attributes:
        name (str) : Name of the scraper that will be used for saved json file.
        courses (List) : List of courses.
        root_url (str) : Root URL where the courses to be scraped. Can be use in links with no root URL.
        url (str) : Full URL where the courses to be scraped.
        driver : Web driver 
    """
    
    name:str = ""
    courses: List = []
    root_url: str = ""
    url:str = ""
    driver = None
    
    """ Initialize driver.
    """
    def __init__(self) -> None:
        self.driver = Driver().driver()
        
    
    def get_courses(self) -> List[Course]:
        """Get scraped list of courses
        """
        return self.courses
    
    
    """ Save scraped courses as json file
    """
    def save_to_json(self):
        obj = self.courses
        file = f"output/{self.name}-courses-{int(time())}.json"

        os.makedirs(os.path.dirname(file), exist_ok=True)

        with open(file, 'w') as json_file:
            json.dump(obj, json_file, default=str)