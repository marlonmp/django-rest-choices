# Rest Choices

## Instalation

```bash
$ pip install django-rest-choices
```

## usage

```python

## apps/my_model/model.py

from django.db import models

class MyModel(models.Model):

    ## ...

    ROLE_ADMIN = 'A'
    ROLE_EMPLOYEE = 'E'

    ROLE_CHOICE = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_EMPLOYEE, 'Employee'),
    )

    ## ...

## urls.py

from django.urls import path

from rest_choices.views import ListChoiceAPIView

urlpatterns = [
    path('/choices/<app_label>.<model>/<choice>', ListChoiceAPIView.as_view()),
]

```

Request example:

[GET] `http://localhost:8000/chices/my_model.MyModel/ROLE_CHOICE` 

Response example:

```json
[
    {
        "code": "A",
        "description": "Admin"
    },
    {
        "code": "E",
        "description": "Employee"
    }
]
```

## Custom list choice

```python

## apps/choices/views.py

from rest_choices.views import ListChoiceAPIView

class CustomListChoice(ListChoiceAPIView):

    def format_choice(self, choice):

        lower_code = choice[0].lower()

        reverse_description = choice[1][::-1]

        return {
            'code': lower_code,
            'description': reverse_description,
        }

## apps/choices/urls.py

from django.urls import path

from .views import CustomListChoice

urlpatterns = [
    path('/custom-choices/<app_label>/<model>/<choice>', CustomListChoice.as_view()),
]

```

Request example:

[GET] `http://localhost:8000/custom-choices/my_model/MyModel/ROLE_CHOICE` 

Response example:

```json
[
    {
        "code": "a",
        "description": "nimdA"
    },
    {
        "code": "e",
        "description": "eeyolpmE"
    }
]
```
