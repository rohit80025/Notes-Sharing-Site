"""NotesSharingProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from notes import views
#from django.conf.static import static
from django.conf.urls.static import static

from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('user_login/',views.user_login,name='user_login'),
    path('login_admin/',views.login_admin,name='login_admin'),
    path('signup/',views.signup1,name='signup'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('logout/',views.Logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('change_password',views.change_password,name='change_password'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('upload_notes',views.upload_notes,name='upload_notes'),
    path('view_mynotes',views.view_mynotes,name='view_mynotes'),
    path('notes/delete/<int:pid>/', views.delete_mynotes, name='delete_mynotes'),
    path('view_users',views.view_users,name='view_users'),
    path('users/delete/<int:pid>/', views.delete_users, name='delete_users'),
    path('pending_nots', views.pending_nots, name='pending_nots'),
    path('accepted_nots', views.accepted_nots, name='accepted_nots'),
    path('rejected_nots', views.rejected_nots, name='rejected_nots'),
    path('all_nots', views.all_nots, name='all_nots'),
    path('assign_status/<int:pid>/', views.assign_status, name='assign_status'),
    path('delete_nots/<int:pid>/', views.delete_nots, name='delete_nots'),
    path('view_all_nots', views.view_all_nots, name='view_all_nots'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


