class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.id = 0
        self.groups = ["Electrical", "Mechanical", "Aerospace", "Civil", "Chemical", "Petroleum"]
        self.users = ["db_user_1", "db_user_2", "db_user_3", "db_user_4", "db_user_5", "db_user_6", "db_user_7",  
                      "db_user_8", "db_user_9", "db_user_10", "db_user_11", "db_user_12", "db_user_13", "db_user_14",
                     "db_user_15", "db_user_16"]
        
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
                for name in group.get_users():
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

sub_child_user = "db_user_17"
sub_child.add_user(sub_child_user)

sub_child_user = "db_user_18"
sub_child.add_user(sub_child_user)

sub_child_user = "db_user_19"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child) 

# Test Cases 

print("Is db_user_1 in Group Electrical?", parent.is_user_in_group("db_user_1", "Electrical"))
print("Is db_user_4 in Group Petroleum?", child.is_user_in_group("db_user_4", "Petroleum"))
print("Is db_user_17 in Group Mechanical?", parent.is_user_in_group("db_user_17", "Mechanical"))
print("Is db_user_5 in Group Chemical?", sub_child.is_user_in_group("db_user_5", "Chemical"))
print("Is db_user_18 in Group Aerospace?: ", child.is_user_in_group("db_user_18", "Aerospace"))
print("get_parent_groups_test: ", parent.get_groups())

# print("sub_child users: ", sub_child.get_users()) 
# print("child users: ", child.get_users())
# print("parent users: ", parent.get_users())

# print("sub_child groups: ", sub_child.get_groups()) 
# print("child groups: ", child.get_groups())
# print("parent groups: ", parent.get_groups())

# Is db_user_1 in Group Electrical? True
# Is db_user_4 in Group Petroleum? True
# Is db_user_17 in Group Mechanical? None
# Is db_user_5 in Group Chemical? True
# Is db_user_18 in Group Aerospace?:  None
# get_parent_groups_test:  ['Electrical', 'Mechanical', 'Aerospace', 'Civil', 'Chemical', 'Petroleum', <__main__.Group object at 0x105110710>]
