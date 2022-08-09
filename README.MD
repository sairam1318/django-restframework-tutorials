#Django Rest Framework basics operation

### Steps to be followed

 1. Create virtualenv using `Virtualenv env` command
 2. Activate virtualenv using `env\Scripts\activate` for windows and for ubunutu `env\bin\activate`
 3. Then install:
    1. pip install djangorestframework
    2. pip install markdown  
    3. pip install django-filter 
 4. Then next:
    1. django-admin startproject djangoLearning . #dot is to create directory in the same folder.
    2. cd djangoLearning
    3. django-admin startapp quickstart
    4. cd ..
 5. Then run `python manage.py migrate` to apply django db changes and run server using ``python manage.py runserver``
 6. Now create models in your app i.e., here in quickstart.
    1. For simplicity, we can create models from existing db tables using ``python manage.py inspectdb {tableName}``
    2. Or we can create a model here and migrate the changes in the db using migrate command.
 7. Once models are done, create the respective serializer class mentioning the models and fields required.
 8. Then create ViewSets in views to perform post, get etc. operations on it.
 9. Then register the url in urls.py in main project.
 10. Then you are good to go 👍