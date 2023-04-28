from django.forms import ModelForm
from .models import Used

class UsedForm(ModelForm):
  class Meta: 
    model = Used
    fields = ['date', 'valmap']