from django.contrib import admin
from .models import Jornal, Categoria, Autor

# Register your models here.
admin.site.register(Jornal)
admin.site.register(Categoria)
admin.site.register(Autor)
