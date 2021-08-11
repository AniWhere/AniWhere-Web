from django.contrib import admin
from django.urls import path
from awapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.main,name="main"),
    path('board/',views.showattractions,name="showattractions"),
    path('bookmark/',views.bookmark,name="bookmark"),
    path('plan/',views.plan,name="plan"),
    path('recommend/',views.recommend,name="recommend"),
    path('search/',views.search,name="search"),
]