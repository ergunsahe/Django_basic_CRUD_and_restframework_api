from django.urls import path

from .views import home_api, StudentList, StudentUpdateDelete
urlpatterns = [
    path("home-api/", home_api, name="home"),
    path("list-create-api/", StudentList.as_view()),
    path("<int:id>/", StudentUpdateDelete.as_view(), name="detail"),
    # path("list-create-api/", student_list_create_api),
    # path("<int:id>/", student_get_update_delete, name="detail"),
    # path("list-api/", student_list_api, name="list"),
    # path("create-api/", student_create_api, name="create"),
]