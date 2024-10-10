Question 1:- By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer:-By default, Django signals are executed synchronously, meaning they run in the same thread as the main code and must finish before the rest of the code can continue. If a signal handler takes time to complete, like waiting or performing a long task, the rest of the program has to wait for it.
Example, if a signal handler has a time.sleep(5) , it will delay everything, and the code will only move forward after those 5 seconds are over. This proves that signals block the main thread and don't run in the background by default.
Example to demonstrate that Django signals are executed synchronously-------

import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal handler started")
    time.sleep(5)  # Simulate a long task
    print("Signal handler finished")
    
print("Starting save operation")
my_model_instance = MyModel.objects.create(name="Test")  # This triggers the post_save signal
print("Save operation complete")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 2:- Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.
Answer:- Yes, Django signals run in the same thread as the code that triggers them. This means that when something like saving a model happens, the signal and the rest of the code run in the same sequence within the same thread. To prove this, we can use Python's threading.get_ident() function to print the thread ID of both the caller and the signal handler. Since the IDs will match, it shows that the signal and the action that triggers it are in the same thread, confirming they are not run separately.
Example to demonstrate that Django signals run in the same thread as the caller----

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")
    import threading
    
print(f"Caller thread ID: {threading.get_ident()}")
my_model_instance = MyModel.objects.create(name="Test")  # This triggers the post_save signal

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Question 3:- By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer:- Django signals do not automatically run in the same database transaction as the main code. This means that if the signal modifies the database, those changes might still be saved, even if an error happens in the main code and causes a rollback.
For example, if a signal adds data to the database and then an error happens in the main code, the data added by the signal might still be saved, while the rest of the transaction gets rolled back. This shows that signals and the main code can run in separate database transactions unless you explicitly put them in the same transaction.  

Code Example:- 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel, AnotherModel
from django.db import transaction

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    # Modify another model in the signal
    AnotherModel.objects.create(name="Signal Change")
    print("Signal handler executed")
    from myapp.models import MyModel

try:
    with transaction.atomic():
        print("Starting save operation")
        my_model_instance = MyModel.objects.create(name="Test")  # This triggers the post_save signal
        # Deliberately raise an error to rollback the transaction
        raise Exception("Intentional error to cause rollback")
except Exception as e:
    print(f"Error occurred: {e}")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                    Topic: Custom Classes in Python

  Question:- Description: You are tasked with creating a Rectangle class with the following requirements:

1. An instance of the Rectangle class requires length:int and width:int to be initialized.
2. We can iterate over an instance of the Rectangle class 
3. When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}

Answer:-
class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    def __iter__(self):
        # We will yield length first, then width
        yield {'length': self.length}
        yield {'width': self.width}
rect = Rectangle(5, 3)
for attr in rect:
    print(attr)




                                         
