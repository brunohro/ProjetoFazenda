"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Fazenda.views import index, listar_animais, cadastrar_animais, editar_animais, remover_animal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('listar_animais/', listar_animais, name="listar_animais"),
    path('cadastrar_animais/', cadastrar_animais, name="cadastrar_animais"),
    path('editar_animais/<int:id>', editar_animais, name="editar_animais"),
    path('remover_animal/<int:id>', remover_animal, name="remover_animal"),
]
