from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class EditGuildForm(FlaskForm):
    prefix = StringField(
        label="Bot Prefix", validators=[DataRequired(), Length(min=1, max=10)]
    )
    submit = SubmitField(label="Update")
