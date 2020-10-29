import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id   =    db.IntField( unique=True)
    first_name  =  db.StringField( max_length=50)
    last_name   = db.StringField( max_length=50)
    email    = db.StringField(max_length=50)
    password  = db.StringField( max_length=50)
    branch = db.StringField( max_length= 50)
    isadmin= db.StringField(max_length= 10)



    def set_password(self, password):
        self.password = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password, password)    

class Contracts(db.Document):
    cont_id   =   db.IntField( unique=True )
    user_id      =   db.IntField(  )
    file_name = db.StringField()
    contract_owner = db.StringField()
    contract_number = db.StringField()
    counterparty= db.StringField()
    entitlement = db.StringField()
    status = db.StringField()
    final_price = db.StringField()
    termination_clause = db.StringField()
    expiry_date= db.StringField()
    signatory= db.StringField()
    role= db.StringField()
    date = db.StringField()
    representative = db.StringField()
    date_recieved  = db.StringField()
    comment1 = db.StringField()
    comment2 = db.StringField()
    comment3 = db.StringField()
    department = db.StringField()
    date_of_review = db.StringField()
    
class Notemp2(db.Document):
    cont_id   =   db.IntField( unique=True )
    user_id      =  db.IntField(  )
    file_name = db.StringField()
    contract_title = db.StringField()
    date_of_review = db.StringField()
    department = db.StringField()
    comment1 = db.StringField()
    comment2 = db.StringField()
    comment3 = db.StringField()
    comment4 = db.StringField()





   
    
    
class Reviewed(db.Document):
    user_id     =   db.IntField()
    cont_id    =   db.StringField( max_length=10 )
    