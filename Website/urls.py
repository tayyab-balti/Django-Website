from django.urls import path
from . import views

urlpatterns = [
    path('my-site/', views.UploadButton, name="mysite"),
    path('my-images/', views.MyImages, name="my_images"),
    path('download-original/', views.download_original, name='download_original'),
    path('download-segmented/', views.download_segmented, name='download_segmented'),
    path('performance-metrics', views.performance_metrics, name='performance_metrics'),
    
    
    
    
    
    path('feedback/', views.FeedbackPage, name="feedback"),
]