class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

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


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

parent.add_user("smith")
new=Group("group1")
parent.add_group(new)
new.add_user("adam")
new.add_user("Professor")


def is_user_in_group(user, group):
    if user in group.users:
        return True
    for grp in group.groups:
        if is_user_in_group(user,grp):
            return True
    return False

print(is_user_in_group("sub_child_user",child))#return True
print(is_user_in_group("adam",new))#return True
print(is_user_in_group("smith",new))#return False
print(is_user_in_group("Professor",child))#return False
print(is_user_in_group("smith",parent))#return True