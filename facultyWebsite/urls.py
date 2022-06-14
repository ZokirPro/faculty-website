"""facultyWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from index.views import *
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('ckeditor_uploader/',include('ckeditor_uploader.urls')),
    path('',index,name='index'),
    path('news/education/',NewsEducationList.as_view(),name='education_news'),
    path('competition/',NewsCompetitionsList.as_view(),name='competition'),
    path('talenteds/', TalentedsList.as_view(),name="talenteds"),
    path('news/<int:id>',news_detail,name='news_detail'),
    path('resources/<int:id>',resources_detail,name='resources_detail'),
    path('talenteds/<int:id>',talenteds_detail,name='talenteds_detail'),
    path('contact/',contact,name='contact'),
    path('qabul/',question_times,name='question_times'),
    path('employees/',EmployeesList.as_view(),name='employees'),
    path('laws/list',LawsList.as_view(),name='law_list'),
    path('rosetta/',include('rosetta.urls')),
    path('about/', about_us,name="about"),
    path('i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
