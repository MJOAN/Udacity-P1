class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.id = 0
        self.groups = ["Electrical", "Mechanical", "Aerospace"]
        self.users = ["db_user_1", "db_user_4", "db_user_10", "db_user_11", "db_user_12", "db_user_13"]
        
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
                    if name == user and user in category: # here
                        continue
                    return True
                return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "db_user_17"
sub_child.add_user(sub_child_user)

sub_child_user = "db_user_18"
sub_child.add_user(sub_child_user)

sub_child_user = "db_user_19"
sub_child.add_user(sub_child_user)

parent_user = "db_user_16" 
parent.add_user(parent_user)

child_user = "db_user_14"
child.add_user(child_user)

parent_user = "db_user_15"
parent.add_user(parent_user)

child.add_group(sub_child)

parent_group =  "Civil"
parent.add_group(parent_group)

child_group =   "Chemical"
child.add_group(child_group)

sub_child_group =  "Petroleum"
sub_child.add_group(sub_child_group)

# Test Cases 

print("Is db_user_1 in Group Electrical?", parent.is_user_in_group("db_user_1", "Electrical")) # True
print("Is db_user_4 in Group Petroleum?", child.is_user_in_group("db_user_4", "Petroleum")) # False
print("Is db_user_17 in Group Mechanical?", parent.is_user_in_group("db_user_17", "Mechanical")) # True
print("Is db_user_5 in Group Chemical?", sub_child.is_user_in_group("db_user_10", "Chemical")) # False
print("Is db_user_18 in Group Aerospace?: ", child.is_user_in_group("db_user_18", "Aerospace")) # True

# print("sub_child users: ", sub_child.get_users()) 
# print("child users: ", child.get_users())
# print("parent users: ", parent.get_users())

# print("sub_child groups: ", sub_child.get_groups()) 
# print("child groups: ", child.get_groups())
# print("parent groups: ", parent.get_groups())

# Is db_user_1 in Group Electrical? True
# Is db_user_4 in Group Petroleum? True
# Is db_user_17 in Group Mechanical? False
# Is db_user_5 in Group Chemical? True
# Is db_user_18 in Group Aerospace?:  False
