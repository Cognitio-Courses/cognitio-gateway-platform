from typing import TypedDict, List
from typing_extensions import NotRequired

class CourseDetails(TypedDict):
    description:str
    link: str
    language: NotRequired[str]
    

class Course(CourseDetails):
    title: str
    summary: str
    image:str
    category: NotRequired[List]
    language: NotRequired[str]
    type: NotRequired[str]



    