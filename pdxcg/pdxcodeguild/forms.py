from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import InlineRadios


class PostForm(forms.Form):
    full_name = forms.CharField(max_length=256)
    phone_number = forms.CharField(max_length=15, required=False)
    email_address = forms.EmailField()
    what_can_we_help_you_acheieve = forms.CharField(widget=forms.Textarea)


class Contact(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Contact, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout("full_name", 'email_address', 'phone_number',InlineRadios('best_contact'), 'message')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    full_name = forms.CharField(
        label="Name:",
        max_length=80,
        required=True,
    )

    email_address = forms.EmailField(
        label="Email:",
        max_length=80,
        required=True,
    )

    phone_number = forms.CharField(
        label="Phone Number:",
        required=False,
    )

    best_contact = forms.ChoiceField(
        choices=(
            ('Phone', "Phone"),
            ('Email', "Email"),
            ('Either', "Either"),
        ),
        label = "How do you prefer to be contacted?",
        widget = forms.RadioSelect,
        initial = 'Either',
    )

    message = forms.CharField(
        label = "What can we help you achieve?",
        required = True,
        widget=forms.Textarea
    )