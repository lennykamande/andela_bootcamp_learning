
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
    def login(self, email, password):
			return next((obj for obj in users if obj.email == email and obj.password == password), none)


    def logout(User):
		"""Logout user from sessions."""
			pass
	@property
    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticate

class Shoppinglist(object):
	
    def __init__(self, title, descripition, date, user_id):
    	self.title = title
    	self.descripition = descripition	
    	self.date = datetime.now().strftime('%Y-%m-%d')
    	self.shopping =[]

    def create(self, title, descripition, date):
    	self.shopping.append('')

