
# Question 1:- All the Answer are README FILE (lin:  https://github.com/anilg199/Accuknox#)



import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  
    print("Signal handler finished")
    
print("Starting save operation")
my_model_instance = MyModel.objects.create(name="Test")  
print("Save operation complete")

