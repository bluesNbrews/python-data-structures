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

    def __str__(self):
        return "This object is named {}.".format(self.name)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    group_list = group.get_groups()
    for g in group_list:
        print(g)
        if not g.groups:
            print("Empty list")
            user_list = g.get_users()
            for u in user_list:
                print(u)
                if u == str(user):
                    print("True")
                    result = True
                else:
                    print("False")
                    result = False
            return result
        if isinstance(g, Group):
            result = is_user_in_group(user, g)
    return result