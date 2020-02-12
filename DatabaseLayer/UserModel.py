from flask_sqlalchemy import SQLAlchemy
from DatabaseLayer.Settings import app
from DatabaseLayer.DataModel import *
from uuid import uuid4

db = SQLAlchemy(app)

class Subscription(db.Model):
    __tablename_ = 'Subscription'
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    CompanyId = db.Column(UUIDType(binary=True), db.ForeignKey(Component.Id), nullable=False)
    Count = db.Column(db.Integer)
    Valid = db.Column(db.Boolean)
    
    def createSubscription(_companyId):
        id = uuid4().hex
        new_subscription = Subscription(Id = id, CompanyId = _companyId, Count = 0, Valid = True)
        db.session.add(new_subscription)
        db.session.commit()
        return id

class User(db.Model):
    __tablename__ = 'Users'
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    Username = db.Column(db.String(80), unique=True, nullable=False)
    Password = db.Column(db.String(80), nullable=False)
    SubscriptionId = db.Column(UUIDType(binary=True), db.ForeignKey(Subscription.Id), nullable=False)
    
    def __repr__(self):
        return str({
            'username': self.Username,
            'password': self.Password
        })
        
    def username_password_match(_username, _password):
        user = User.query.filter_by(Username=_username).filter_by(Password=_password).first()
        if user is None:
            return False
        else:
            return True
        
    def getAllUsers():
        return User.query.all()
    
    def createUser(_username, _password,_subscriptionId):
        id = uuid4().hex
        new_user = User(Id=id, Username=_username, Password=_password, SubscriptionId = _subscriptionId)
        db.session.add(new_user)
        db.session.commit()
        return id