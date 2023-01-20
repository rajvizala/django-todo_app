from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CreateUserForm(UserCreationForm):


    # This code is to make the email field required in html form 
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True

    class Meta:
        model = User
        fields = ['email','username','password1','password2']
