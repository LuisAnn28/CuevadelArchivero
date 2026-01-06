from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'libros'

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('crear/', views.agregar_libro, name='crear'),
    path('<int:pk>/', views.detalle_libro, name='detalle'),
    path('<int:pk>/editar/', views.editar_libro, name='editar'),
    path('<int:pk>/borrar/', views.eliminar_libro, name='eliminar'),
    path('login/', auth_views.LoginView.as_view(
        template_name='libros/login.html'
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('populares/', views.libros_populares, name='libros_populares'),
    path('autores/', views.autores_populares, name='autores_populares'),
    path('registro/', views.registro, name='registro'),
]