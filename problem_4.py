class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.id = 0
        self.groups = ["Electrical", "Mechanical", "Aerospace", "Civil", "Chemical", "Petroleum"]
        self.users = ["Adrien", "Beck", "Christoff", "David", "Ellen", "Ferdinand", "Geoff",  
                      "Harry", "Inna", "Jason", "Ken", "Leonard", "Mary", "Nannette",
                     "Quentin", "Raphael"]
        
    def add_group(self, group):
        self.groups.append(group)
    
    def add_user(self, user):
        self.users.append(user)
    
    def get_groups(self):  
        return self.groups 
    
    def get_users(self): 
        return self.users
    
    def get_name(self):  
        return self.name
    
    def is_user_in_group(self, user, group):

        for category in self.get_groups():
            if category == group: 
                for name in self.get_users():
                    if name == user:
                        return True
                    return False
                    
parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "Sam"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child) 

print("sub_child users: ", sub_child.get_users()) 
print("child users: ", child.get_users())
print("parent users: ", parent.get_users())

print("sub_child groups: ", sub_child.get_groups()) 
print("child groups: ", child.get_groups())
print("parent groups: ", parent.get_groups())

print("def parent Sam: ", parent.is_user_in_group("Sam", "Electrical"))
print("def child Kevin: ", child.is_user_in_group("Ken", "Petroleum"))
print("get_parent_groups: ", parent.get_groups())