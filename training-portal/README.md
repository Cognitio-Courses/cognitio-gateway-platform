# training-gateway

## Install app dependencies
```console
    pip install -r requirements.txt
```

## Migrate tables
```console
    python manage.py migrate
    python manage.py initdata
    python manage.py initpermissions
```

## Initialize Skill level, Thematic areas, Tools data and group permission
```console
    python manage.py initdata
    python manage.py initpermissions
```

## Create super user
```console
    python manage.py createsuperuser
```


> Note: Newly registered `Content Creator` must be activated first in Django Admin site using a `superuser`.
Check `is_active`.



### Users
username | password| account |
---------|---------|---------|
testuser | admin   | trainee
ccreator | admin   | content_creator
admin    | admin   | superuser/admin