from django.contrib.auth.forms import UserCreationForm
from app.models import Account



class SignupForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('email',)