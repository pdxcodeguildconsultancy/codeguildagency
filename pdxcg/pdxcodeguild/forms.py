from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import InlineRadios
from .models import NewStudentApplication
from django.core.validators import RegexValidator

class NewStudentApp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewStudentApp, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    first_name = forms.CharField(
        max_length=255,
        label="Name:",
        required=True,
    )

    middle_initial = forms.CharField(
        max_length=1
    )
    last_name = forms.CharField(
        max_length=255
    )
    date_of_birth = forms.DateField(
        auto_now=False
    )
    street_address = forms.CharField(
        max_length=255
    )
    city = forms.CharField(
        max_length=255
    )
    state = forms.CharField(
        max_length=255
    )

    zip = forms.IntegerField(
        max_length=5
    )

    applied_before = forms.BooleanField()

    if_yes_app = forms.DateField(
        auto_now=False
    )

    attended_before = forms.BooleanField()

    if_yes_grad = forms.CharField(
        max_length=255
    )

    if_no_grad = forms.Textarea(
    )

    phone_number = forms.CharField(
        validators=[phone_regex],
        blank=True
    )

    message_number = forms.CharField(
        validators=[phone_regex],
        blank=True
    )

    cell_number = forms.CharField(
        validators=[phone_regex],
        blank=True
    )

    email = forms.EmailField()
    us_citizen = forms.BooleanField()

    # Emergency Contact Information

    contact_name = forms.CharField(
        max_length=255
    )

    contact_address = forms.CharField(
        max_length=255
    )

    contact_city = forms.CharField(
        max_length=255
    )

    contact_state = forms.CharField(
        max_length=255
    )

    contact_zip = forms.CharField(
        max_length=255
    )

    contact_number = forms.CharField(
        validators=[phone_regex],
        blank=True
    )



    class Meta:
        model = NewStudentApplication







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
        label="How do you prefer to be contacted?",
        widget=forms.RadioSelect,
        initial='Either',
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
        self.helper.layout = Layout("name", 'email_address', InlineRadios('first'), InlineRadios('second'),
                                    InlineRadios('third'), InlineRadios('fourth'), InlineRadios('fifth'),
                                    InlineRadios('sixth'), InlineRadios('seventh'), InlineRadios('eighth'),
                                    InlineRadios('ninth'), InlineRadios('tenth'), 'message1', 'message2')
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
        label="Depth of the Knowledge of the subject",
        widget=forms.RadioSelect,
    )

    second = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Presentation Skills",
        widget=forms.RadioSelect,
    )

    third = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Sincerity, Commitment, Regularity and Punctuality",
        widget=forms.RadioSelect,
    )

    fourth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Syllabus Coverage",
        widget=forms.RadioSelect,
    )

    fifth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Ability to Clarify doubts, teaching with relevant examples",
        widget=forms.RadioSelect,
    )

    sixth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Ability to relate the course to real life situations",
        widget=forms.RadioSelect,
    )

    seventh = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Ability to generate interest",
        widget=forms.RadioSelect,
    )

    eighth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Accessibility of teachers for doubts and clarifications outside the class",
        widget=forms.RadioSelect,
    )

    ninth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Ability to command and control the class",
        widget=forms.RadioSelect,
    )

    tenth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label="Overall teacher rating",
        widget=forms.RadioSelect,
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


class StudentIntake(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StudentIntake, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout('name', 'email_address', 'git_hub', 'student_bio', 'student_goals')
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    name = forms.CharField(
        label="Name:",
        max_length=80,
        required=True,
    )

    email_address = forms.EmailField(
        label="Email:",
        max_length=80,
        required=True,
    )

    git_hub = forms.CharField(
        label='GitHub URL:',
        max_length=200,
        required=True,
    )

    student_bio = forms.CharField(
        label='Tell us a little about yourself.',
        required=False,
        widget=forms.Textarea,
    )

    student_goals = forms.CharField(
        label= 'Tell us about your goals for this class.',
        required=False,
        widget=forms.Textarea,
    )