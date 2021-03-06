from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Regsiration Form
class RegistratonForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'first_name',
                  'last_name']
