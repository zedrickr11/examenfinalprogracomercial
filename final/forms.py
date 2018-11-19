from django import forms

from .models import Grado, Materia



class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ('nombre', 'seccion', 'Materia')

    def __init__ (self, *args, **kwargs):
        super(GradoForm, self).__init__(*args, **kwargs)
        self.fields["Materia"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["Materia"].help_text = "Ingrese las materias que desea cursar"
        self.fields["Materia"].queryset = Materia.objects.all()
