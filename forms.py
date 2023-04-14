from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, URL, Length, Regexp


class ApplicationForm(FlaskForm):
  full_name = StringField('Full Name',
                          validators=[
                            DataRequired(),
                            Length(min=1, max=250),
                            Regexp(regex="[a-zA-Z]",
                                   message="Incorrect Data format")
                          ])
  #email = StringField('Email', validators=[Email()])
  # linkedin_url = StringField('LinkedIn URL',
  #                            validators=[DataRequired(), URL()])
  # education = TextAreaField('Education', validators=[DataRequired()])
  # work_experience = TextAreaField('Work Experience',
  #                                 validators=[DataRequired()])
  # resume_url = StringField('Resume URL', validators=[DataRequired(), URL()])
  submit = SubmitField('Submit')
