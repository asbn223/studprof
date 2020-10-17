from django import forms


class StudentForm(forms.Form):
    """Add Student Form"""

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'field',
                'placeholder': 'Your Name'
            }
        )
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'field',
                'placeholder': 'Your Age'
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'field',
                'placeholder': 'Your Phone'
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'field',
                'placeholder': 'Your Email'
            }
        )
    )
