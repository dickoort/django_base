from django.db import models
from django.contrib.auth.models import User

# standaard User model extenden:
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='remate_django_baseapp/profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username


# Simple data model where customers order MenuItems on various dates...
class Customer(models.Model):
    customer_name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.customer_name + " --- " + self.url

class MenuItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #name = models.CharField(max_length=264,unique=True)
    name = models.CharField(max_length=264,unique=False)
    def __str__(self):
        return self.name

class OrderDate(models.Model):
    name = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

#
# ###### CRM system maken ooit!!
# class CompanyAccount(models.Model):
#     company_name = models.CharField(max_length=264,unique=True)
#     company_website = models.URLField(unique=True)
#
# class CompanyContact(models.Model):
#     company = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE)
#     contact_first_name = models.CharField(max_length=264,unique=True)
#     contact_second_name = models.CharField(max_length=264,unique=True)
#     contact_phone =  models.CharField(max_length=12,unique=True)
#     #https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
#
# class Visit(models.Model):
#     company_contact = models.ForeignKey(CompanyContact, on_delete=models.CASCADE)
#     visit_date = models.DateField()
#     visit_report = models.CharField(max_length=500,unique=True)
#
# #
# # o = Order(name="  ", date="" , status="X")
# #
# class Order(models.Model):
#     company_name = models.ForeignKey(CompanyAccount, on_delete=models.CASCADE)
#     order_name = models.CharField(max_length=60)
#     start_date = models.DateField()
#     STATUS_CHOICES = (
#         ('O', 'Opportunity, not engaged'),
#         ('E', 'Engaged by phone or e-mail'),
#         ('I', 'Incoming lead'),
#         ('H', 'Hot lead'),
#         ('S', 'Sold'),
#         ('C', 'Closed'),
#     )
#     order_status = models.CharField(max_length=1, choices=STATUS_CHOICES)
