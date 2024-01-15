from django_registration.forms import RegistrationForm
from blango_auth.models import User
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class BlangoRegistrationForm(RegistrationForm):
  class Meta(RegistrationForm.Meta):
    model=User

  def __init__(self, *args, **kwargs):
    super(BlangoRegistrationForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit("submit", "Register"))

  