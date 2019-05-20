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
                    if name is None:
                        return False
                    if name != user:
                        continue
                    elif name == user:
                        return True
                    else:
                        return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "Sam"
sub_child.add_user(sub_child_user)

sub_child_user = "Travis"
sub_child.add_user(sub_child_user)

sub_child_user = "Uri"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child) 

print("Is Sam in Group Electrical?", parent.is_user_in_group("Sam", "Electrical"))
print("Is Kevin in Group Petroleum?", child.is_user_in_group("Kevin", "Petroleum"))
print("Is Nannette in Group Mechanical?", parent.is_user_in_group("Nannette", "Mechanical"))
print("Is Inna in Group Chemical?", sub_child.is_user_in_group("Inna", "Chemical"))
print("Is Travis in Group Aerospace?: ", child.is_user_in_group("Travis", "Aerospace"))
print("get_parent_groups_test: ", parent.get_groups())

# print("sub_child users: ", sub_child.get_users()) 
# print("child users: ", child.get_users())
# print("parent users: ", parent.get_users())

# print("sub_child groups: ", sub_child.get_groups()) 
# print("child groups: ", child.get_groups())
# print("parent groups: ", parent.get_groups())