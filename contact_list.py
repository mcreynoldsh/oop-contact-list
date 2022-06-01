from functools import cmp_to_key
def sort_by_name(a,b):
    
    if a["name"] < b["name"]:
        return -1
    elif a["name"] > b["name"]:
        return 1
    else:
        return 0  

class ContactList():
    def __init__(self, name, contact_list):
        self.name = name
        self.contact_list= contact_list
        self.sort_list()

    def add_contact(self,contact):
        self.contact_list.append(contact)
        self.sort_list()

    def remove_contact(self,cont_name):
        for n in self.contact_list:
            if n["name"] == cont_name:
                self.contact_list.remove(n)    

    def sort_list (self):
        self.contact_list= sorted(self.contact_list, key= cmp_to_key(sort_by_name))

    def print_contacts(self):
        for x in self.contact_list:
            print(x)  

    def find_shared_contacts(self,cont_list):
        shared_contacts = []
        for k in cont_list.contact_list:
            if self.contact_list.count(k) > 0 :
                shared_contacts.append(k)
        return shared_contacts         



friends = [{'name':'Alice','number':'867-5309'},{'name':'Zack', 'number':'555-5460'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

# my_friends_list.print_contacts()
# my_friends_list.remove_contact("Bob")
# my_friends_list.print_contacts()

friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)     

print(friends_i_work_with)