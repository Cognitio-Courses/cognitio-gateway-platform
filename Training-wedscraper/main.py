from typing import List
from fastapi import FastAPI
from scraper.eocollege_scraper import EOCollegeScraper
from scraper.esa_scraper import EsaCourseScraper
from scraper.moocs_scraper import MoocsCourseScraper
from scraper.arset_scraper import ARSETScraper

from scraper.typings import Course, CourseDetails

app = FastAPI()


@app.get("/esa")
def courses() -> List[CourseDetails]:
    scraper = EsaCourseScraper()
    return scraper.get_courses()

@app.get("/moocs")
def moocs_courses():
    scraper = MoocsCourseScraper()
    return scraper.get_courses()


@app.get("/eo-college")
def moocs_courses():
    scraper = EOCollegeScraper()
    return scraper.get_courses()


@app.get("/arset")
def moocs_courses():
    scraper = ARSETScraper()
    return scraper.get_courses()
