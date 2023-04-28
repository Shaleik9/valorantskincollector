from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Skin, Buddy
from .forms import UsedForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request): 
  return render(request, 'about.html')

def skins_index(request):
  skins = Skin.objects.all()
  return render(request, 'skins/index.html', {'skins': skins})  

def skins_detail(request, skin_id):
  skin = Skin.objects.get(id=skin_id)
  id_list = skin.buddies.all().values_list('id')
  buddies_skin_doesnt_have = Buddy.objects.exclude(id__in=id_list)
  used_form = UsedForm()
  return render(request, 'skins/detail.html', {'skin': skin, 'used_form': used_form, 'buddies': buddies_skin_doesnt_have})

class SkinCreate(CreateView):
  model = Skin
  fields = ['collection', 'weapon', 'edition', 'limited', 'chromas', 'price']

class SkinUpdate(UpdateView):
  model = Skin
  fields = ['weapon', 'edition', 'limited', 'chromas', 'price']

class SkinDelete(DeleteView):
  model = Skin
  success_url = '/skins'

def add_used(request, skin_id):
  form = UsedForm(request.POST)
  if form.is_valid():
    new_used = form.save(commit=False)
    new_used.skin_id = skin_id
    new_used.save()
  return redirect('detail', skin_id=skin_id)

class BuddyList(ListView):
  model = Buddy

class BuddyDetail(DetailView):
  model = Buddy

class BuddyCreate(CreateView):
  model = Buddy
  fields = '__all__'

class BuddyUpdate(UpdateView):
  model = Buddy
  fields = ['name', 'color']

class BuddyDelete(DeleteView):
  model = Buddy 
  success_url = '/buddies'

def assoc_buddy(request, skin_id, buddy_id):
  Skin.objects.get(id=skin_id).buddies.add(buddy_id)
  return redirect('detail', skin_id=skin_id)

def unassoc_buddy(request, skin_id, buddy_id):
  Skin.objects.get(id=skin_id).buddies.remove(buddy_id)
  return redirect('detail', skin_id=skin_id)
