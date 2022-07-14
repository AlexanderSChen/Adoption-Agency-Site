from flask_wtf import FlaskForm 
from wtforms import StringField, TextAreaField, BooleanField, IntegerField, RadioField, SelectField 
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Name", validators=[InputRequired(message="Pet Name cannot be blank")])

    species = SelectField("Pet Species", choices=[('dog', 'dog'), ('cat', 'cat'), ('pc', 'porcupine')])

    photo_url = StringField("Picture of Pet", validators=[Optional(), URL()])

    age = IntegerField("Pet's Current Age", validators=[Optional(), NumberRange(min=0, max=30)])
    
    notes = StringField("Notes on Pet: allergies, diseases, etc.", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form for editing existing pet"""

    name = StringField("Name", validators=[InputRequired(message="Pet Name cannot be blank")])

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])

    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")