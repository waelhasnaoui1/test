from flask import Resource 
from models.store import StoreModel 

class Store(Resorce):
    def get (self,name): 
       store = StoreModel.find_by_name(name)
       if store : 
           return store.json() 
       return {'message' : 'store not found '},404

    def post (self,name): 
        if StoreModel.find_by_name(name): 
            return {'message' : "A store with name {} already exist".format(name)}
        store = StoreModel(name)
        try : 
            store.save_to_db()
        except : 
            return {'message' : 'An error occured when saving'},500
        return store.json()
    
    def delete (self,name): 
        store = StoreModel.find_by_name(name)
        if store : 
            store.delete_from_db()
        return {'message' : 'store deleted'}


class StoreList(Resource): 
    def get (self): 
        return {'stores' : [store.json() for store in StoreModel.query.all()]}