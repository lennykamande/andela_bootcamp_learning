
users = []
class User(object):

    def __init__(self, firstname, lastname, username, email, password):
    	self.username = username
    	self.email = email	
    	self.password = password
    	self.firstname = firstname
    	self.lastname = lastname
		
    def register(self, username, firstname, lastname, email, password):
			x = users.append(username, firstname, password, email, lastname )
			print x
    def login(self, ):
			pass

    def logout(User):
			pass


class Shoppinglist(object):
	
    def __init__(self, title, descripition, date, user_id):
    	self.title = title
    	self.descripition = descripition	
    	self.date = datetime.now().strftime('%Y-%m-%d')
    	self.shopping =[]

    def create(self, title, descripition, date):
    	self.shopping.append('')

