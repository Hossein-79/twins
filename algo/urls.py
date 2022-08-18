"""algo URL Configuration

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
from twins import views

urlpatterns = [
    path('', views.index),
    path('all_applications/', views.all_applications),
    path('search_application/', views.search_application),
    path('application/<int:app_id>', views.get_application),
    path('get_repo/', views.get_repo_contract_files),
    path('check/', views.check_application),

    path('choose/', views.choose_repo_file),
    path('check_app/', views.check_application),
    path('admin/', admin.site.urls),
]
