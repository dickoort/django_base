import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','remate_django_base.settings')

import django
# Import settings
django.setup()

import random
from remate_django_baseapp.models import Customer,MenuItem,OrderDate
from faker import Faker

fakegen = Faker()
customers = ['John','Maria','Petra','Ruben','Yoran']

def add_customer():
    c = Customer.objects.get_or_create(customer_name=random.choice(customers))[0]
    c.url = fakegen.url()
    c.save()
    return c



def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Get Customer
        cust = add_customer()
        print(cust)
        print(str(cust))

        # Create Fake Data for entry
#        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.last_name()

        # Create new MenuItem Entry
        menu_item_entry = MenuItem.objects.get_or_create(customer=cust,name=fake_name)[0]

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = OrderDate.objects.get_or_create(name=menu_item_entry,date=fake_date)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
