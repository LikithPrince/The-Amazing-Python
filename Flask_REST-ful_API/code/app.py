
from flask import Flask , request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app=Flask(__name__)
app.secret_key='liki'
api=Api(app)

jwt=JWT(app, authenticate, identity)

items=[]



class Item(Resource):
    @jwt_required()
    def get(self, name):
        item=next(filter(lambda x:x['name']==name, items),None)      
        return {"item": item}, 200 if item else 404
    
    
    def post(self, name):
        if next(filter(lambda x:x['name']==name, items),None):
            return {'message': f"An item with name {name} is already exists "},400
        data=request.get_json()
        item={'name':name,'price':data['price']}
        items.append(item)
        return item , 201

    def put(self, name):
        data=request.get_json()
        item=next(filter(lambda x:x['name']==name, items),None)
        if item is None:
            item={'name':name,'price':data['price']}
            items.append(item)
        item.update(data)
        return item , 201

    def delete(self, name):
        global items
        items=list(filter(lambda x:x['name']!=name, items))
        return {'message':"Item Deleted"}
        

class ItemList(Resource):
    def get(self):
        return {'items': items}





api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

if __name__=='__main__':
    app.run(debug=True)

