# Question 2: Describe in the README file. Only code is here.


import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
import threading
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")


print(f"Caller thread ID: {threading.get_ident()}")
my_model_instance = MyModel.objects.create(name="Test")  

