from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from sqlalchemy_utils import UUIDType
from uuid import uuid4
import json
from DatabaseLayer.Settings import app

db = SQLAlchemy(app)

class Company(db.Model):
    __tablename_ = 'Company'
    Name = db.Column(db.String(80), nullable=False)
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    SubscriptionId =db.Column(UUIDType(binary=True), nullable=False) 
    
    def json(self):
        return{'Name':self.Name, 'Id':self.Id, 'SubscriptionId':self.SubscriptionId} 
    
    def add_company(_name, _id, _subscriptionId):
        new_company = Company(Name=_name, Id=_id, SubscriptionId=_subscriptionId)
        db.session.add(new_company)
        db.session.commit()
        
    def get_all_companies():
        return[Company.json(company) for company in Company.query.all()] 
    
    def get_company_by_id(_id):
        return Company.query.filter_by(Id=_id).first()
    
    def delete_company(_id):
        Company.query.filter_by(Id=_id).delete()
        db.session.commit()
        
    def update_company(_name, _id, _subscriptionId):
        company_to_update = Company.query.filter_by(Id=_id)
        company_to_update.Name = _name
        company_to_update.SubscriptionId = _subscriptionId
        db.session.commit()    
    
    def __repr__(self):
        company_object ={
            'Name':self.Name,
            'Id':self.Id,
            'SubscriptionId':self.SubscriptionId
        } 
        return json.dumps(company_object)
    
class Product(db.Model):
    __tablename_ = 'Product'
    Name = db.Column(db.String(80), nullable=False)
    Id = db.Column(UUIDType(binary=True), primary_key=True)
    CompanyId = db.Column(UUIDType(binary=True), db.ForeignKey(Company.Id), nullable=False) 

    def add_product(_name, _id, _companyId):
        new_product = Product(Name=_name, Id=_id, CompanyId=_companyId)
        db.session.add(new_product)
        db.session.commit()
        
    def get_all_products():
        return Product.query.all()
    
    def get_Product_by_id(_id):
        return Product.query.filter_by(Id=_id).first()
    
    def delete_product(_id):
        Product.query.filter_by(Id=_id).delete()
        db.session.commit()
        
    def update_product(_name, _id, _companyId):
        product_to_update = Product.query.filter_by(Id=_id)
        product_to_update.Name = _name
        product_to_update.CompanyId = _companyId
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
    
    def add_device(_name, _id, _productId):
        new_device = Device(Name=_name, Id=_id, ProductId=_productId)
        db.session.add(new_device)
        db.session.commit()
        
    def get_all_devices():
        return Device.query.all()
    
    def get_device_by_id(_id):
        return Device.query.filter_by(Id=_id).first()
    
    def delete_device(_id):
        Device.query.filter_by(Id=_id).delete()    
        db.session.commit()
        
    def update_device(_name, _id, _productId):
        device_to_update = Device.query.filter_by(Id=_id)
        device_to_update.Name = _name
        device_to_update.ProductId = _productId
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
    
    def add_component(_name, _id, _deviceId):
        new_component = Component(Name=_name, Id=_id, DeviceId=_deviceId)
        db.session.add(new_component)
        db.session.commit()
        
    def get_all_components():
        return Component.query.all()
    
    def get_component_by_id(_id):
        return Component.query.filter_by(Id=_id).first()
    
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
    timeStamp = db.Column(db.TIMESTAMP, primary_key=True, nullable=False)
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
    timeStamp = db.Column(db.TIMESTAMP, db.ForeignKey(Data.timeStamp), nullable=False)
    resultTimeStamp = db.Column(db.TIMESTAMP, primary_key=True, nullable=False)
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
        return Result.json(Result.query.filter_by(componentId=_componentId).first())    
    
    def get_data_by_timestamp(_componentId, _timeStamp):
        return Result.json(Result.query.filter_by(componentId=_componentId, timeStamp= _timeStamp).first())
    
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