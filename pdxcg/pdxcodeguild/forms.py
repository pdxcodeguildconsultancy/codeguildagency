from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Fieldset, Layout, HTML
from crispy_forms.bootstrap import InlineRadios
from froala_editor.widgets import FroalaEditor

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
        self.helper.label_class = 'col-lg-3 smalltext'
        self.helper.field_class = 'col-lg-7'
        self.helper.layout = Layout(
            Fieldset('',
                "name",
                'email_address',
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                HTML("""
                    <p style="text-align: center;">Please rate the following on a scale of 1 to 4.</p>
                    <p style="text-align: center;">1 = Poor, 2 = Fair, 3 = Good, 4 = Excellent</p>
                    """),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('first'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('second'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('third'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('fourth'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('fifth'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('sixth'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('seventh'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('eighth'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('ninth'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div>
                    """),
                InlineRadios('tenth'),
                HTML("""
                <div style="border: 0; height: 2px; background: #fff; background-image: -webkit-linear-gradient(left,
                #fff, #fff, #fff); background-image: -moz-linear-gradient(left, #fff, #fff, #fff); background-image:
                 -ms-linear-gradient(left, #fff, #fff, #fff); background-image: -o-linear-gradient(left, #fff, #fff,
                 #fff);"></div><br>
                    """),
                'message1',
                'message2',))
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    name = forms.CharField(
        label="Name (optional):",
        max_length=80,
        required=False,
    )

    email_address = forms.EmailField(
        label="Email (optional):",
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
        label = "Depth of the Knowledge of the subject:",
        required=False,
        widget = forms.RadioSelect,
    )

    second = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Presentation Skills:",
        required=False,
        widget = forms.RadioSelect,
    )

    third = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Sincerity, Commitment, Regularity and Punctuality:",
        required=False,
        widget = forms.RadioSelect,
    )

    fourth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Syllabus Coverage:",
        required=False,
        widget = forms.RadioSelect,
    )

    fifth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to Clarify doubts, teaching with relevant examples:",
        required=False,
        widget = forms.RadioSelect,
    )

    sixth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to relate the course to real life situations:",
        required=False,
        widget = forms.RadioSelect,
    )

    seventh = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to generate interest:",
        required=False,
        widget = forms.RadioSelect,
    )

    eighth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Content and length of lectures:",
        required=False,
        widget = forms.RadioSelect,
    )

    ninth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Ability to command and control the class:",
        required=False,
        widget = forms.RadioSelect,
    )

    tenth = forms.ChoiceField(
        choices=(
            ('1', "1"),
            ('2', "2"),
            ('3', "3"),
            ('4', "4"),
        ),
        label = "Overall teacher rating:",
        required=False,
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

