from django import forms

from accounts.validators import allow_only_images_validator
from .models import Category, PlantItem


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'description']


class PlantItemForm(forms.ModelForm):
    image = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info w-100'}), validators=[allow_only_images_validator])
    class Meta:
        model = PlantItem
        fields = ['category', 'plant_title', 'description', 'price', 'image', 'is_available']