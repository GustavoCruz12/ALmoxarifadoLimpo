from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ('username', 
                  'name', 
                  'email',
                  'almoxarifado_user', 
                  'secretaria_user', 
                  'departamento_user',
                  'user_permissions',
                  )

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])