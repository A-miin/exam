from django import forms

# from .models import Product
# CATEGORY_CHOICES=[
#     ('breakfast','завтрак'),
#     ('first meal','первые блюда'),
#     ('second courses','вторые блюда'),
#     ('drinks','напитки '),
#     ('other','разное'),
# ]
#
# class ProductForm(forms.ModelForm):
#
#     class Meta:
#         model = Product
#         fields = ('name', 'description', 'category', 'price', 'remainder')


class RecordSearchForm(forms.Form):
    name = forms.CharField(max_length=128, label = "Введите имя")