from unittest.util import _MAX_LENGTH
from django import forms
class ToDoListForm(forms.Form):
    text = forms.CharField(max_length=45,
            widget=forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g Grocery shopping',
                'arialabel': 'ToDo', 'aria-describeby' :'add-bnt'}))