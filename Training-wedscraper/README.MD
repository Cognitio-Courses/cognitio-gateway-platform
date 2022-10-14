# Course Scraper

Running API server.
```console

uvicorn main:app --reload
```

## API Endpoints

|URL       | Course platform            |
|----------|----------------------------|
|`/esa`    | Eeuropean Space Agency     |
|`/moocs`  | Massive Open Onlone Courses|
|`/eo-college`| Earth Observation College|
| `/arset`| Applied Remote Sensing Training Program|


## Class Methods

`save_to_json` : Save file to a json file.

`get_courses`: Get list of scraped data.