from django.contrib import admin
from final.models import Profesor, Alumno, Materia, Grado, MateriaAdmin, GradoAdmin
# Register your models here.
admin.site.register(Profesor)
admin.site.register(Alumno)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Grado, GradoAdmin)
