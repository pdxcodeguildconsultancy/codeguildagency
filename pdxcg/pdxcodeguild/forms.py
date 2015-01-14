from django import forms
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import InlineRadios
from django.core.validators import RegexValidator
from django.forms.extras.widgets import SelectDateWidget
from captcha.fields import ReCaptchaField
import datetime
from .models import NewStudentApplication, StudentIntake, SkillAssessment


class NewStudentApp(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewStudentApp, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    QUESTION_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    BIRTH_YEARS = (
        2015,
        2014,
        2013,
        2012,
        2011,
        2010,
        2009,
        2008,
        2007,
        2006,
        2005,
        2004,
        2003,
        2002,
        2001,
        2000,
        1999,
        1998,
        1997,
        1996,
        1995,
        1994,
        1993,
        1992,
        1991,
        1990,
        1989,
        1988,
        1987,
        1986,
        1985,
        1984,
        1983,
        1982,
        1981,
        1980,
        1979,
        1978,
        1977,
        1976,
        1975,
        1974,
        1973,
        1972,
        1971,
        1970,
        1969,
        1968,
        1967,
        1966,
        1965,
        1964,
        1963,
        1962,
        1961,
        1960,
        1959,
        1958,
        1957,
        1956,
        1955,
        1954,
        1953,
        1952,
        1951,
        1950,
    )

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
        max_length=1,
        required=False,
    )
    last_name = forms.CharField(
        max_length=255,
        required=True,
    )
    date_of_birth = forms.DateField(
        widget=SelectDateWidget(years=BIRTH_YEARS),
        required=True,
    )
    street_address = forms.CharField(
        max_length=255,
        required=True,
    )
    city = forms.CharField(
        max_length=255,
        required=True,
    )
    state = forms.CharField(
        max_length=255,
        required=True,
    )

    zip = forms.IntegerField(
        required=True,
    )

    applied_before = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        required=True,
    )

    if_yes_app = forms.DateField(
        widget=SelectDateWidget(years=BIRTH_YEARS),
        required=False,
    )

    attended_before = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        required=True,
    )

    if_yes_grad = forms.CharField(
        max_length=255,
        required=False,
    )

    if_no_grad = forms.Textarea(
    )

    phone_number = forms.CharField(
        validators=[phone_regex],
    )

    message_number = forms.CharField(
        validators=[phone_regex],
        required=False,
    )

    cell_number = forms.CharField(
        validators=[phone_regex],
        required=False,
    )

    email = forms.EmailField(
        required=True,
    )
    us_citizen = forms.ChoiceField(
        choices=QUESTION_CHOICES,
        required=True,
    )

    # Emergency Contact Information

    contact_name = forms.CharField(
        max_length=255,
        required=True,
    )

    contact_address = forms.CharField(
        max_length=255,
        required=True,
    )

    contact_city = forms.CharField(
        max_length=255,
        required=True,
    )

    contact_state = forms.CharField(
        max_length=255,
        required=True,
    )

    contact_zip = forms.CharField(
        max_length=255,
        required=True,
    )

    contact_number = forms.CharField(
        validators=[phone_regex],
        required=True,
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
                                    'message', 'captcha')
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

    captcha = ReCaptchaField(
        attrs={'theme': 'clean'}
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


class StudentIntakeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentIntakeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout('name', 'email_address', 'instructor_name', 'git_hub', 'student_bio',
                                    'student_goals')
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

    instructor_name = forms.CharField(
        label="Instructor's Name:",
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
        label='Tell us about your goals for this class.',
        required=False,
        widget=forms.Textarea,
    )

    class Meta:
        model = StudentIntake


class SkillAssessmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SkillAssessmentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-7'
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

    instructor_name = forms.CharField(
        label="Instructor's Name:",
        max_length=80,
        required=True,
    )
    date = forms.DateField(widget=SelectDateWidget(), initial=datetime.date.today())
    skill_level = forms.ChoiceField(
        choices=(
            ('1. Little to no knowledge.', "1. Little to no knowledge."),
            ('2. A general understanding that allows you to get work done.',
             "2. A general understanding that allows you to get work done."),
            ('3. You are very knowledgeable.', "3. You are very knowledgeable."),
        ),
        label="Please check the number that best matches your skill level.",
        widget=forms.RadioSelect,
    )

    # General Skills
    management = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Computer Management Creating, Copying, Moving and Deleting Files and Folders",
        widget=forms.RadioSelect,
    )

    internals = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Computer Internals (RAM, Disks, CPU, etc)",
        widget=forms.RadioSelect,
    )

    command_line = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Command Line (cd, ls/dir, cp/copy, md/mkdir, etc)",
        widget=forms.RadioSelect,
    )

    networking = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Computer Networking (DNS, IP Addresses, etc)",
        widget=forms.RadioSelect,
    )

    written_communication = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="General Written Communication",
        widget=forms.RadioSelect,
    )

    math = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="General Math (Pre Algebra)",
        widget=forms.RadioSelect,
    )

    logic = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="General Logic (Reasoning, Deduction)",
        widget=forms.RadioSelect,
    )

    spreadsheets = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Spreadsheets (Excel, etc)",
        widget=forms.RadioSelect,
    )

    user_databases = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="User Databases (MS Access, etc)",
        widget=forms.RadioSelect,
    )

    editors_ide = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Code Editors and IDE's",
        widget=forms.RadioSelect,
    )

    html = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="HTML",
        widget=forms.RadioSelect,
    )

    css = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="CSS",
        widget=forms.RadioSelect,
    )

    # Code Skills
    variables_datatypes = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Variables and Datatypes (String, Int, Etc)",
        widget=forms.RadioSelect,
    )

    flow_control = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Flow Control (If, then, else, switch, case)",
        widget=forms.RadioSelect,
    )

    functions = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Functions",
        widget=forms.RadioSelect,
    )

    classes_objects = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Classes and Objects",
        widget=forms.RadioSelect,
    )

    design_patterns = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Design Patterns (MVC, etc)",
        widget=forms.RadioSelect,
    )

    debugging = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Debugging",
        widget=forms.RadioSelect,
    )

    source_control = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Source code control",
        widget=forms.RadioSelect,
    )

    profiling_performance_optimization = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
            ('5', "5"),
        ),
        label="Profiling and performance optimization",
        widget=forms.RadioSelect,
    )

    what_do_you_hope_we_cover = forms.CharField(
        label='What do you hope to cover?',
        required=False,
        widget=forms.Textarea,
    )

    what_skills_do_you_want_to_acquire = forms.CharField(
        label='What skills do you want to acquire?',
        required=False,
        widget=forms.Textarea,
    )

    projects_applications_in_mind = forms.CharField(
        label='What projects and practical applications do you have in mind?',
        required=False,
        widget=forms.Textarea,
    )

    class Meta:
        model = SkillAssessment