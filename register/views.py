from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Register, Character, Weapon
from django.urls import reverse_lazy

# Create your views here.
class RegisterList(ListView):
    template_name = 'list.html'
    model = Register


class RegisterDetail(DetailView):
    template_name = 'detail.html'
    model = Register


class RegisterCreate(CreateView):
    template_name = 'create.html'
    model = Register
    fields = ('character', 'dmg', 'rank', 'mw', 'sw', 'member1', 'member2')
    success_url = reverse_lazy('list')


class CharaCreate(CreateView):
    template_name = 'cratecharacter.html'
    model = Character
    fields = ('name', 'use')
    success_url = reverse_lazy('list')


class WeaponCreate(CreateView):
    template_name = 'cratecharacter.html'
    model = Weapon
    fields = ('name', 'kind', 'bullet')
    success_url = reverse_lazy('list')


class RegisterDelete(DeleteView):
    template_name = 'delete.html'
    model = Register
    success_url = reverse_lazy('list')


class RegisterUpdate(UpdateView):
    template_name = 'update.html'
    model = Register
    fields = ('character', 'dmg', 'rank', 'mw', 'sw', 'member1', 'member2')
    success_url = reverse_lazy('list')

