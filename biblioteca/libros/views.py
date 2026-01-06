from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, "libros/lista_libros.html", {
        "libros": libros,
        "mostrar_nav": True,
        'mostrar_header': False
    })

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/detalle_libro.html', {'libro': libro, 'mostrar_nav': True, 'mostrar_header': False})

@login_required
def agregar_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros:lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form, 'accion': 'Crear', 'mostrar_nav': True, 'mostrar_header': False})

@login_required
def editar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros:detalle', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/libro_form.html', {'form': form, 'accion': 'Editar', 'mostrar_nav': True, 'mostrar_header': False})

@login_required
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros:lista_libros')
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro, 'mostrar_nav': True, 'mostrar_header': False})

def home(request):
    return render(request, "libros/home.html", {
        "mostrar_header": True
    })

def lista_externa(request, titulo, items):
    return render(request, 'libros/populares.html', {
        'titulo': titulo,
        'items': items
    })

def libros_populares(request):
    items = [
        {
            "titulo": "Dune",
            "imagen": "imagenes/dune.jpg",
            "link": "https://es.wikipedia.org/wiki/Dune"
        },
        {
            "titulo": "1984",
            "imagen": "imagenes/1984.jpg",
            "link": "https://es.wikipedia.org/wiki/1984_(novela)"
        },
                {
            "titulo": "Problema de los tres cuerpos",
            "imagen": "imagenes/tres_cuerpos.jpg",
            "link": "https://es.wikipedia.org/wiki/El_problema_de_los_tres_cuerpos"
        },
                        {
            "titulo": "Maldita",
            "imagen": "imagenes/maldita.jpg",
            "link": "https://books.google.com.mx/books/about/Maldita.html?id=e6q5DwAAQBAJ&source=kp_book_description&redir_esc=y"
        },
                {
            "titulo": "Momo",
            "imagen": "imagenes/momo.jpg",
            "link": "https://es.wikipedia.org/wiki/Momo_(novela)"
        },
                {
            "titulo": "Diablo Guardián",
            "imagen": "imagenes/guardian.jpg",
            "link": "https://es.wikipedia.org/wiki/Diablo_Guardi%C3%A1n"
        },
                {
            "titulo": "It (Eso)",
            "imagen": "imagenes/it.jpg",
            "link": "https://es.wikipedia.org/wiki/It_(novela)"
        },
    ]
    return render(request, "libros/populares.html", {
    "titulo": "Libros populares",
    "items": items,
    "mostrar_nav": False,
})



def autores_populares(request):
    items = [
        {
            "nombre": "Frank Herbert",
            "imagen": "imagenes/frank_herbert.jpg",
            "link": "https://es.wikipedia.org/wiki/Frank_Herbert"
        },
        {
            "nombre": "Liu Cixin",
            "imagen": "imagenes/liu_cixin.jpg",
            "link": "https://es.wikipedia.org/wiki/Liu_Cixin"
        },
        {
            "nombre": "Thomas Wheeler",
            "imagen": "imagenes/thomas.jpg",
            "link": "https://en.wikipedia.org/wiki/Tom_Wheeler_(writer)"
        },
        {
            "nombre": "Michael Ende",
            "imagen": "imagenes/ende.jpg",
            "link": "https://en.wikipedia.org/wiki/Michael_Ende"
        },
        {
            "nombre": "Xavier Velasco",
            "imagen": "imagenes/xaviervelasco.jpg",
            "link": "https://es.wikipedia.org/wiki/Xavier_Velasco"
        },
        {
            "nombre": "Stephen King",
            "imagen": "imagenes/king.jpg",
            "link": "https://en.wikipedia.org/wiki/Stephen_King"
        },
        {
            "nombre": "George Orwell",
            "imagen": "imagenes/orwell.jpg",
            "link": "https://es.wikipedia.org/wiki/George_Orwell"
        },
    ]
    return render(request, "libros/populares.html", {
    "titulo": "Autores más leídos",
    "items": items,
    "mostrar_nav": False,
})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'registration/registro.html', {'form': form})


