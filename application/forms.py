from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from application.models import User, Contracts, Notemp2

class LoginForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6,max=15)])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email   = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(), Length(min=2, max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=55)])
    branch = StringField("Branch", validators=[DataRequired(), Length(min=2, max=55)])
    isadmin = StringField("Is Admin (True/ False)", validators=[DataRequired(), Length(min=2, max=55)])
    submit = SubmitField("Register Now")

    def validate_email(self,email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError("Email is already in use. Pick another one.")

    # def validate_email(self,email):
    #     user = User.objects(email=email.data).first()
    #     if user:
    #         raise ValidationError("Email is already in use. Pick another one.")
class Contracts(FlaskForm):
    file_name = StringField()
    contract_owner = StringField()
    contract_number = StringField()
    counterparty= StringField()
    entitlement = StringField()
    status = StringField()
    final_price =StringField()
    termination_clause = StringField()
    expiry_date= StringField()
    signatory= StringField()
    role= StringField()
    date = StringField()
    representative = StringField()
    date_recieved  = StringField()
    comment1 = StringField()
    comment2 = StringField()
    comment3 = StringField()
    department = StringField()
    date_of_review = StringField()
        

class Notemp2(FlaskForm):
    file_name = StringField()
    contract_title = StringField()
    date_of_review = StringField()
    department = StringField()
    comment1 = StringField()
    comment2 = StringField()
    comment3 = StringField()
    comment4 = StringField()
 
    
