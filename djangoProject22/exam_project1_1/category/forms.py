from django import forms

from exam_project1_1.category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class CreateCategoryForm(CategoryForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if Category.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError("Category name must be unique (case-insensitive).")
        return name
