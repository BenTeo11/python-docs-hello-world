from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy_utils import UUIDType
from uuid import uuid4
import json
from DatabaseLayer.Settings import app
#from DatabaseLayer.UserModel import *

db = SQLAlchemy()

class Company(db.Model):
    __tablename_ = 'Company'
    Name = db.Column(db.String(80), nullable=False)
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    SubscriptionId =db.Column(UUIDType(binary=True), nullable=True) 
    
    def json(self):
        return{'Name':self.Name, 'Id':str(self.Id), 'SubscriptionId':str(self.SubscriptionId)}          
    
    def add_company(_name, _id, _subscriptionId):
        new_company = Company(Name=_name, Id=_id, SubscriptionId=_subscriptionId)
        db.session.add(new_company)
        db.session.commit()
        
    def get_all_companies():
        return[Company.json(company) for company in Company.query.all()]  
    
    def get_company_by_id(_id):
        return Company.json(Company.query.filter_by(Id=_id).first())
    
    def get_company_by_name(_name):
        return[Company.json(company) for company in Company.query.filter_by(Name=_name)]    
    
    def delete_company(_id):
        Company.query.filter_by(Id=_id).delete()
        db.session.commit()
        
    def update_company(_name, _id, _subscriptionId):
        company_to_update = Company.query.filter_by(Id=_id)
        company_to_update.Name = _name
        company_to_update.SubscriptionId = _subscriptionId
        db.session.commit()
        
    def createCompany(_name):
        id = uuid4().hex
        new_company = Company(Id = id, Name = _name, SubscriptionId = None)       
        db.session.add(new_company)
        db.session.commit()            
    
    def __repr__(self):
        company_object ={
            'Name':self.Name,
            'Id':str(self.Id),
            'SubscriptionId':str(self.SubscriptionId)
        } 
        return json.dumps(company_object)
    
class Product(db.Model):
    __tablename_ = 'Product'
    Name = db.Column(db.String(80), nullable=False)
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    CompanyId = db.Column(UUIDType(binary=True), db.ForeignKey(Company.Id), nullable=False) 
    
    def json(self):
        return{'Name':self.Name, 'Id':str(self.Id), 'CompanyId':str(self.CompanyId)}       

    def add_product(_name, _id, _companyId):
        new_product = Product(Name=_name, Id=_id, CompanyId=_companyId)
        db.session.add(new_product)
        db.session.commit()
        
    def get_all_products():
        return[Product.json(product) for product in Product.query.all()] 
    
    def get_product_by_id(_id):
        return Product.json(Product.query.filter_by(Id=_id).first())
    
    def delete_product(_id):
        Product.query.filter_by(Id=_id).delete()
        db.session.commit()
        
    def update_product(_name, _id, _companyId):
        product_to_update = Product.query.filter_by(Id=_id)
        product_to_update.Name = _name
        product_to_update.CompanyId = _companyId
        db.session.commit()
        
    def createProduct(_name, _companyId):
        id = uuid4().hex
        new_product = Product(Id = id, Name = _name, CompanyId = _companyId)
        db.session.add(new_product)
        db.session.commit()            
    
    def __repr__(self):
        product_object ={
            'Name':self.Name,
            'Id':self.Id,
            'CompanyId':self.CompanyId
        } 
        return json.dumps(product_object)    

class Device(db.Model):
    __tablename_ = 'Device'
    Name = db.Column(db.String(80), nullable=False)
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    ProductId = db.Column(UUIDType(binary=True), db.ForeignKey(Product.Id), nullable=False)
    
    def json(self):
        return{'Name':self.Name, 'Id':str(self.Id), 'ProductId':str(self.ProductId)}       
    
    def add_device(_name, _id, _productId):
        new_device = Device(Name=_name, Id=_id, ProductId=_productId)
        db.session.add(new_device)
        db.session.commit()
                
    def get_all_devices():
        return[Device.json(device) for device in Device.query.all()] 
    
    def get_device_by_id(_id):
        return Device.json(Device.query.filter_by(Id=_id).first())
    
    def delete_device(_id):
        Device.query.filter_by(Id=_id).delete()    
        db.session.commit()
        
    def update_device(_name, _id, _productId):
        device_to_update = Device.query.filter_by(Id=_id)
        device_to_update.Name = _name
        device_to_update.ProductId = _productId
        db.session.commit()
        
    def createDevice(_name, _productId):
        id = uuid4().hex
        new_device = Device(Id = id, Name = _name, ProductId = _productId)
        db.session.add(new_device)
        db.session.commit()                 
    
    def __repr__(self):
        device_object ={
            'Name':self.Name,
            'Id':self.Id,
            'ProductId':self.ProductId
        } 
        return json.dumps(device_object)    

class Component(db.Model):
    __tablename_ = 'Component'
    Name = db.Column(db.String(80), nullable=False)
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    DeviceId = db.Column(UUIDType(binary=True), db.ForeignKey(Device.Id), nullable=False)

    def json(self):
        return{'Name':self.Name, 'Id':str(self.Id), 'DeviceId':str(self.DeviceId)}
    
    def add_component(_name, _id, _deviceId):
        new_component = Component(Name=_name, Id=_id, DeviceId=_deviceId)
        db.session.add(new_component)
        db.session.commit()
        
    def get_all_components():
        return[Component.json(component) for component in Component.query.all()] 
    
    def get_component_by_id(_id):
        return Component.json(Component.query.filter_by(Id=_id).first()) 
    
    def delete_component(_id):
        Component.query.filter_by(Id=_id).delete()
        db.session.commit()
        
    def update_component(_name, _id, _deviceId):
        component_to_update = Component.query.filter_by(Id=_id)
        component_to_update.Name = _name
        component_to_update.DeviceId = _deviceId
        db.session.commit() 
        
    def createComponent(_name, _deviceId):
        id = uuid4().hex
        new_component = Component(Id = id, Name = _name, DeviceId = _deviceId)
        db.session.add(new_component)
        db.session.commit()
    
    def __repr__(self):
        component_object ={
            'Name':self.Name,
            'Id':self.Id,
            'DeviceId':self.DeviceId
        } 
        return json.dumps(component_object)    

class Data(db.Model):
    __tablename_ = 'Data'
    componentId = db.Column(UUIDType(binary=True), db.ForeignKey(Component.Id), nullable=False)
    timeStamp = db.Column(db.DATETIME, primary_key=True, nullable=False)
    data = db.Column(db.NVARCHAR) 
    
    def json(self):
        return{'componentId':str(self.componentId), 'timeStamp':str(self.timeStamp), 'data':self.data}     
    
    def add_data(_timestamp, _componentId, _data):        
        new_data = Data(componentId=_componentId, timeStamp=_timestamp, data=_data)
        db.session.add(new_data)
        db.session.commit()
        
    def get_all_data():
        return [Data.json(data) for data in Data.query.all()] 
    
    def get_data_by_id(_componentId):
        return Data.json(Data.query.filter_by(componentId=_componentId).first())    
    
    def get_data_by_timestamp(_componentId, _timeStamp):
        return Data.json(Data.query.filter_by(componentId=_componentId, timeStamp= _timeStamp).first())
    
    def get_data_the_lastrows(counts,_componentId):       
        return [Data.json(data) for data in Data.query.filter_by(componentId=_componentId).order_by(desc(Data.timeStamp)).limit(counts).all()] 
    
    def delete_data(_timeStamp):
        Data.query.filter_by(timeStamp=_timeStamp).delete()
        db.session.commit()
    
    def __repr__(self):
        data_object ={
            'componentId':str(self.componentId),
            'timeStamp':str(self.timeStamp),
            'data':self.data
        } 
        return json.dumps(data_object)       
       
class Result(db.Model):
    __tablename_ = 'Result'
    componentId = db.Column(UUIDType(binary=True), db.ForeignKey(Component.Id), nullable=False)
    timeStamp = db.Column(db.DATETIME, db.ForeignKey(Data.timeStamp), nullable=False)
    resultTimeStamp = db.Column(db.DATETIME, primary_key=True, nullable=False)
    data = db.Column(db.NVARCHAR) 
    
    def json(self):
        return{'componentId':str(self.componentId), 'timeStamp':str(self.timeStamp), 'resultTimeStamp':str(self.resultTimeStamp), 'data':self.data}     
    
    def add_data(_timestamp, _resultTimeStamp, _componentId, _data):        
        new_data = Result(componentId=_componentId, timeStamp=_timestamp, resultTimeStamp=_resultTimeStamp,data=_data)
        db.session.add(new_data)
        db.session.commit()
        
    def get_all_data():
        return [Result.json(data) for data in Result.query.all()] 
    
    def get_data_by_id(_componentId):
        return [Result.json(data) for data in Result.query.filter_by(componentId=_componentId).order_by(desc(Result.timeStamp)).all()]    
    
    def get_data_by_timestamp(_componentId, _timeStamp):
        return Result.json(Result.query.filter_by(componentId=_componentId, timeStamp= _timeStamp).all())
    
    def get_data_the_lastrows(counts,_componentId):       
        return [Result.json(data) for data in Result.query.filter_by(componentId=_componentId).order_by(desc(Result.timeStamp)).limit(counts).all()] 
    
    def delete_data(_resultTimeStamp):
        Result.query.filter_by(timeStamp=_resultTimeStamp).delete()
        db.session.commit()
    
    def __repr__(self):
        data_object ={
            'componentId':self.componentId,
            'timeStamp':str(self.timeStamp),
            'resultTimeStamp':str(self.resultTimeStamp),
            'data':self.data
        } 
        return json.dumps(data_object)        
    
class Subscription(db.Model):
    __tablename_ = 'Subscription'
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    CompanyId = db.Column(UUIDType(binary=True), db.ForeignKey(Company.Id), nullable=False)
    Count = db.Column(db.Integer)
    Valid = db.Column(db.Boolean)
    
    def createSubscription(_companyId):
        id = uuid4().hex
        new_subscription = Subscription(Id = id, CompanyId = _companyId, Count = 0, Valid = True)
        db.session.add(new_subscription)
        db.session.commit()
        return id
    
    def addSubscription(_companyId, _id):
        new_subscription = Subscription(Id = _id, CompanyId = _companyId, Count = 0, Valid = True)
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