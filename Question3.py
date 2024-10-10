# Question3: This question are describe in the README file. Only code is here.


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, AnotherModel
from myapp.models import MyModel
from django.db import transaction

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    
    AnotherModel.objects.create(name="Signal Change")
    print("Signal handler executed")



try:
    with transaction.atomic():
        print("Starting save operation")
        my_model_instance = MyModel.objects.create(name="Test") 
        raise Exception("Intentional error to cause rollback")
except Exception as e:
    print(f"Error occurred: {e}")
