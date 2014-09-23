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
        self.helper.layout = Layout("full_name", 'email_address', 'phone_number', InlineRadios('best_contact'),
                                    'message')
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
        label="What can we help you achieve?",
        required=True,
        widget=forms.Textarea
    )


class Comment(forms.Form):
    def __init__(self, *args, **kwargs):
        super(Comment, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout("Name", 'email_address', InlineRadios('first'), InlineRadios('second'),
                                    InlineRadios('third'), InlineRadios('fourth'), InlineRadios('fifth'),
                                    InlineRadios('sixth'), InlineRadios('seventh'), InlineRadios('eighth'),
                                    InlineRadios('ninth'), InlineRadios('tenth'), 'message1', 'message1')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    name = forms.CharField(
        label="Name:",
        max_length=80,
        required=False,
    )

    email_address = forms.EmailField(
        label="Email:",
        max_length=80,
        required=False,
    )

    first = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Depth of the Knowledge of the subject",
        widget = forms.RadioSelect,
    )

    second = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Presentation Skills",
        widget = forms.RadioSelect,
    )

    third = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Sincerity, Commitment, Regularity and Punctuality",
        widget = forms.RadioSelect,
    )

    fourth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Syllabus Coverage",
        widget = forms.RadioSelect,
    )

    fifth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to Clarify doubts, teaching with relevant examples",
        widget = forms.RadioSelect,
    )

    sixth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to relate the course to real life situations",
        widget = forms.RadioSelect,
    )

    seventh = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to generate interest",
        widget = forms.RadioSelect,
    )

    eighth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Accessibility of teachers for doubts and clarifications outside the class",
        widget = forms.RadioSelect,
    )

    ninth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to command and control the class",
        widget = forms.RadioSelect,
    )

    tenth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Overall teacher rating",
        widget = forms.RadioSelect,
    )

    message1 = forms.CharField(
        label="What can we do in the future to improve this class?",
        required=False,
        widget=forms.Textarea
    )

    message2 = forms.CharField(
        label="Is there any other suggestion or issues you would like to bring up?",
        required=False,
        widget=forms.Textarea
    )

