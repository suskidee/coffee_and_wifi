from django import forms
from .models import Cafe


class CafeForm(forms.ModelForm):
    class Meta:
        model = Cafe
        fields = ['cafe', 'city', 'location', 'open', 'close', 'coffee', 'wifi', 'power']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.add_input(Submit('submit', 'Send'))
