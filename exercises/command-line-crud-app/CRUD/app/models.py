from django.db import models

# Create your models here.
class Shopping(models.Model):
    item = models.TextField()
    quantity = models.TextField()

def create_item(item, quantity):
    creating_item = Shopping(item=item, quantity=quantity)
    creating_item.save()
    return creating_item
def view_all():
    all_items = Shopping.objects.all()
    return all_items
def search_quantity(quantity):
    item = Shopping.objects.filter(quantity=quantity)  
    return item  
def search_item_name(item):
    try:
        find_item_name = Shopping.objects.get(item=item)
        return find_item_name
    except:
        return None
def update_item(item, new_quantity):
    updating_item = Shopping.objects.get(item=item)
    updating_item.quantity = new_quantity
    updating_item.save()
    return updating_item
def delete_item(item):
    deleting_item = Shopping.objects.get(item=item)
    deleting_item.delete()
    return deleting_item