from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    website = StringField('Website', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    def validate_website(self, form, field):
        regex = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        if not regex.match(field.data):
            raise ValidationError("Please enter a valid email")