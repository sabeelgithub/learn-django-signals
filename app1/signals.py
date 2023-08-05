from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile



@receiver(pre_save,sender=User)
def pre_save_signle_handle(sender,instance,**kwargs):
    print(f'Hi,{instance.username} we are going to save your credential')
    if instance.first_name:
        print('you already have user name')
    else:
        instance.first_name = 'dummy_first'
        print(f'we are assigned a dummy first name for you,ie is {instance.first_name}')

@receiver(post_save,sender=User)
def post_save_signal_handle(sender,instance,created,**kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance,address='dummyAddress',place='dummyPlace',district='dummyDistrict',state='dummyState')
        profile.save()
        print('your profile also created')
    else:
        print('no changes made to your profile,while you are updating your credential')

@receiver(pre_delete,sender=User)
def pre_delete_signal_handle(sender,instance,**kwargs):
    print(f'we are going to delete {instance.username} credential')


@receiver(post_delete,sender=User)
def post_delete_signale_handle(sender,instance,**kwargs):
    print(f'user with id {instance.id} is deleted')

    


        




# user1 = User(email='anshida@gmail.com',username='anshida')
# user2 = User(email='konshida@gmail.com',username='konshida')
# user1.save()
# user2.save()
# print(user1.get_username())
# print(user2.get_username())
# print(user1.delete())
# print(user2.delete())




