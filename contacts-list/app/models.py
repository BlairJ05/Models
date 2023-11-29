from django.db import models
#this is a comment
# Create your models here.
class Contact(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone = models.CharField(max_length=10)
    is_favorite = models.BooleanField(True)

def create_contact(name, email, phone, is_favorite):
    contact = Contact(name=name, email=email, phone=phone, is_favorite=is_favorite)
    contact.save()
    return contact

def all_contacts():
    all_contacts = Contact.objects.all()
    return all_contacts

def find_contact_by_name(user_name):
        try:
            find_name = Contact.objects.get(name=user_name)
            return find_name
        except:
             return None
    
def favorite_contacts():
    contacts = Contact.objects.filter(is_favorite=True)
    return contacts

def update_contact_email(user_name, new_email):
    contact = Contact.objects.get(name=user_name)
    contact.email = new_email
    contact.save()
    return contact

def delete_contact(user_name):
    contact = Contact.objects.get(name=user_name)
    contact.delete()
    return contact