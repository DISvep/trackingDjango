from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Task, Comment


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'image', 'media', 'status', 'priority', 'deadline']
        widgets = {
            "name": forms.TextInput(attrs={
                'class': 'form-control'
            }),
            "description": forms.Textarea(attrs={
                'class': 'form-control'
            }),
            "image": forms.FileInput(attrs={
                'class': 'form-control'
            }),
            "media": forms.FileInput(attrs={
                'class': 'form-control'
            }),
            "status": forms.Select(attrs={
                'class': 'form-control'
            }),
            "priority": forms.Select(attrs={
                'class': 'form-control'
            }),
            "deadline": forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'}
            ),
        }


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'Всі'),
        ('_expired', 'Вичерпане'),
        ('_in_progress', 'В процесі'),
        ('_done', 'Завершене'),
    ]
    PRIORITY_CHOICES = [
        ('', 'Всі'),
        ('_low', 'Низький'),
        ('_mid', 'Середній'),
        ('_high', 'Високий'),
    ]

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        required=False,
        label='Статус',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    priority = forms.ChoiceField(
        choices=PRIORITY_CHOICES,
        required=False,
        label='Пріоритет',
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', "image", 'media']
        labels = {'content': '', 'image': '', 'media': ''}
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'cols': 50,
                'placeholder': 'Type comment...'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control d-none',
                'id': 'id_image_input'
            }),
            'media': forms.FileInput(attrs={
                'class': 'form-control d-none',
                'id': 'id_media_input'
            })
        }
