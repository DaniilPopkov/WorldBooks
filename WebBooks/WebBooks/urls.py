"""
URL configuration for WebBooks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from catalog import views
from django.urls import re_path
from django.urls import path, include 


urlpatterns = [
    path('',views.index),
    path('index_1',views.index_1, name='index_1'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('authors_add/', views.authors_add, name='authors_add'), 
    path('admin/', admin.site.urls),
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^authors/$', views.AuthorListView.as_view(), name='authors'), 
]
urlpatterns += [ 
    path('accounts/', include('django.contrib.auth.urls')), 
    path('edit1/<int:id>/', views.edit1, name='edit1'), 
    path('create/', views.create, name='create'), 
    path('delete/<int:id>/', views.delete, name='delete'),
    # boot_start...
    path('start1/', views.boot_start_page, name='start1'),
    path('color_bg/', views.boot_start_page1, name='color_bg'),
    path('color_text/', views.boot_start_page2, name='color_text'),
    path('color_text_bg/', views.boot_start_page3, name='color_text_bg'),
    path('space_1/',views.space_start_page, name='space_1'),
    path('space_2/',views.space_start_page1, name='space_2'),
    path('space_3/',views.space_start_page2, name='space_3'),
    path('aligment_1/',views.aligment_start_page, name='aligment_1'),
    path('aligment_2/',views.aligment_start_page1, name='aligment_2'),
    path('border_1/',views.border_start_page, name='border_1'),
    path('border_2/',views.border_start_page1, name='border_2'),
    path('border_color/',views.border_color_page, name='border_color'),
    path('border_radius/',views.border_radius_page, name='border_radius'),
    path('border_radius_1/',views.border_radius_page1, name='border_radius_1'),
    path('start/', views.start_start_page, name='start'),
    path('start_1/', views.start_start_page1, name='start_1'),
    path('table/',views.table_start_page, name='table'),
    path('table_1/',views.table_start_page1, name='table_1'),
    

] 
urlpatterns += [ 
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'), 
] 
urlpatterns += [ 
    re_path(r'^book/create/$', views.BookCreate.as_view(), name='book_create'), 
    re_path(r'^book/update/(?P<pk>\d+)$', views.BookUpdate.as_view(), name='book_update'), 
    re_path(r'^book/delete/(?P<pk>\d+)$', views.BookDelete.as_view(), name='book_delete'),
] 