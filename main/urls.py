
from django.urls import path
from . import views



app_name='main'     #다른 앱의 동일한 urlpattern과 중복되지않게
urlpatterns=[
    #name을 지정해 url 별칭을 만들어준다.
    path('', views.index, name='index'),
    path('<int:question_id>/',views.detail, name='detail'),
    path('answer/create/<int:question_id>/',views.answer_create, name='answer_create'),
    path('question/create/',views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),

]