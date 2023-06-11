from django.urls import path 
from. import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('upload/', views.upload, name='upload'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('assessment/', views.assessment, name='assessment'),
    path('add_to_certificate/<int:id>/<str:value>/', views.add_to_certificate, name='add_to_certificate'),
    path('add-new-question/', views.add_new_question, name='add_new_question'),
    path('pending-questions/', views.pending_questions, name='pending_questions'),
    path('approve-question/<int:id>/', views.approve_question, name='approve_question'),
    path('reject-question/<int:id>/', views.reject_question, name='reject_question'),
    path('public-believes/', views.public_believes, name='public_believes'),
    path('reasons/<int:id>/', views.reasons, name='reasons'),
    path('download-certificate/', views.download_certificate, name='download_certificate'),
    path('reasons-opinion/<int:id>/', views.reasons_opinion, name='reasons_opinion'),
    path('category', views.category, name='category'),
    path('category-question/<int:id>/', views.category_question, name='category_question'),
    path('add-comment/<int:id>/', views.add_comment, name='add_comment'),
    path('delete-comment/<int:id>/', views.delete_comment, name='delete_comment'),
    path('update-believes/<int:id>/', views.update_believes, name='update_believes'),
]
