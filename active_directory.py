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
    #Handle cases for no user or no group
    if user == "":
        return "no user provided"

    if group == "":
        return "no group provided"

    group_list = group.get_groups()
    for g in group_list:
        if not g.groups:
            user_list = g.get_users()
            for u in user_list:
                if u == str(user):
                    result = True
                else:
                    result = False
            return result
        if isinstance(g, Group):
            result = is_user_in_group(user, g)
    return result

if __name__ == "__main__":

    parent = Group("parent")
    child_a = Group("child_a")
    child_b = Group("child_b")
    sub_child_1 = Group("subchild1")
    sub_child_2 = Group("subchild2")

    sub_child_user_a = "sub_child_user_a"
    sub_child_user_b = "sub_child_user_b"
    sub_child_user_c = "sub_child_user_c"

    parent.add_group(child_a)
    parent.add_group(child_b)

    child_a.add_group(sub_child_1)
    child_b.add_group(sub_child_2)

    sub_child_1.add_user(sub_child_user_a)
    sub_child_1.add_user(sub_child_user_b)
    sub_child_2.add_user(sub_child_user_c)

    #Test Case 1
    search_result = is_user_in_group("sub_child_user_c", parent)
    print("The search result is {}.".format(search_result))
    #Expected Output: The search result is True.

    #Test Case 2
    search_result = is_user_in_group("sub_child_user_d", parent)
    print("The search result is {}.".format(search_result))
    #Expected Output: The search result is False.

    #Test Case 3
    search_result = is_user_in_group("", parent)
    print("The search result is {}.".format(search_result))
    #Expected Output: The search result is no user provided.

    #Test Case 4
    search_result = is_user_in_group("sub_child_user_c", "")
    print("The search result is {}.".format(search_result))
    #Expected Output: The search result is no group provided.
