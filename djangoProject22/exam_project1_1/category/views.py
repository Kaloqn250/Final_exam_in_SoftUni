from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from exam_project1_1.category.forms import CreateCategoryForm
from exam_project1_1.category.models import Category


# Create your views here.
class CreateCategoryView(CreateView):
    model = Category
    form_class = CreateCategoryForm
    template_name = 'categories/create_category.html'
    success_url = reverse_lazy('event_create')
