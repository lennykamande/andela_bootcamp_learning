#Class user to handle signup and login and register
from random import *
class User(object):
   
    userlist = []

    def __init__(self):
        self.details={}


    def signup(self,username, email, password):
        self.username = username
        self.email = email
        self.password = password
        for user in self.userlist:
            if username == user['username'] or email == user['email']:
                return "username or email exists"
        else:
            self.details ={'username' : self.username, 'email' : self.email , 'password' :  self.password}
            self.userlist.append(self.details)
            print(self.userlist)
            return "registered"


    def login(self,email, password):
        self.email = email
        self.password = password
        for user in self.userlist:
            if email == user['email']:
                print (user)
                if user['password'] == password:
                    return True
        else:
            return False
shoppinglists = []		
class Shoppinglist(object):
   
    

    def __init__(self ):
        
        self.listsdict = {}

    def newlist(self, name, description, owner):
        """ a method to add a new list with the unique user"""
        id = randint(1, 1000)
        self.listsdict = {'name' : name, 'owner' : owner, 'description' : description, 'id' : id}
        shoppinglists.append(dict(self.listsdict))
        print(shoppinglists, "here")
        res = 'success'
        return res

    def view_lists(self, owner):
        """ a method to show lists belonging to a particular user"""
        [items for items in a if d['name'] == 'pluto']
        for items in shoppinglists:
            if items['owner']== owner:
                return items
        else:
            return 'No Items'

shoppingitems = []
class ShoppingItems(object):
   
    

    def __init__(self ):
        
        self.itemsdict = {}
    """ a method to add items belonging to a specific shopping list"""
    def new_item(self, name, description, list_id):
            self.itemsdict = {'name' : name, 'list_id' : list_id, 'description' : description, 'item_id' : item_id}
            shoppingitems.append(self.itemsdict)
            print(shoppingitems, "here")
            res = 'success'
            return res

    """ a method to show items belonging to a specific shopping list"""
    def view_item(self, id):
        for items in shoppingitems:
            if items['id']== id:
                return items
        else:
            return 'No Items'


    """ a method to delete items in a particular list"""
    def delete_item(self, item_id):
        for items in shoppingitems:
            if items['item_id']== item_id:
                return items
        else:
            return 'No Items'