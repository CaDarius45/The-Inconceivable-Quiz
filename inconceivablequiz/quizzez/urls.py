from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('accounts/signup/', views.signup, name='signup'),
    path('info', views.instructions, name='info'),
    path('menu', views.menu, name='menu'),
    path('comunity', views.comunity, name='comunity'),
    #====================Quiz route=========================
    path('quizzes', views.quiz_index, name='quiz-index'),
    path('quizzes/<int:quiz_id>', views.quiz_detail, name='quiz-detail'),
    path('quizzes/create', views.QuizCreate.as_view(), name='quiz-create'),
    path('quizzes/<int:pk>/update', views.quizUpdate.as_view(), name='quiz-update'),
    path('quizzes/<int:pk>/delete', views.quizDelete.as_view(), name='quiz-delete'),
    #====================Question route=========================
    #path('quizzes/<int:quiz_id>/add-question', views.add_question, name='add-question'),

    path('questions', views.QuestionList.as_view(), name='question-index'),
    path('questions/<int:pk>', views.QuestionDetail.as_view(), name='question-detail'),
    path('questions/create', views.QuestionCreate.as_view(), name='question-create'),
    path('questions/<int:pk>/update', views.QuestionUpdate.as_view(), name='question-update'),
    path('questions/<int:pk>/delete', views.QuestionDelete.as_view(), name='question-delete'),
    path('quizzes/<int:quiz_id>/add-question/<int:question_id>/', views.add_question, name='add-question'),
    path('quizzes/<int:quiz_id>/remove-question/<int:question_id>/', views.remove_question, name='remove-question')
]