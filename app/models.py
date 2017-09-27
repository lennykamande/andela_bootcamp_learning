class User(object):

    def __init__(self, firstname, lastname, username, email, password):
    	self.username = username
    	self.email = email	
    	self.password = password
    	self.firstname = firstname
    	self.lastname = lastname
        self.users = []
    	
    
    def register(self, username, email, password, firstname, lastname):
    	self.users.append(username,email,password,firstname,lastname)
        return self.users[firstname]
  
    def login(self, email, password):
    	pass
  
    def logout(self, username,):
    	pass


class Shoppinglist(object):
	
    def __init__(self, title, descripition, date, user_id):
    	self.title = title
    	self.descripition = descripition	
    	self.date = datetime.now().strftime('%Y-%m-%d')
    	self.shopping =[]

    def create(self, title, descripition, date):
    	self.shopping.append('')

