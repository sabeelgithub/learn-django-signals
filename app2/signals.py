from django.db.models.signals import m2m_changed
from django.dispatch import receiver,Signal
from .models import Book,Author

@receiver(m2m_changed, sender=Book.authors.through)
def book_authors_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'post_add':
        # Perform actions after authors are added to the book
        print(f"Authors added to {instance}: {', '.join([str(model.objects.get(pk=pk)) for pk in pk_set])}")
    elif action == 'post_remove':
        # Perform actions after authors are removed from the book
        print(f"Authors removed from {instance}: {', '.join([str(model.objects.get(pk=pk)) for pk in pk_set])}")
    elif action == 'pre_add':
        print(f"Authors going to add to {instance}: {', '.join([str(model.objects.get(pk=pk)) for pk in pk_set])}")
    elif action == 'pre_remove':
        print(f"Authors going to remove to {instance}: {', '.join([str(model.objects.get(pk=pk)) for pk in pk_set])}")
    elif action == 'pre_clear':
        print(f"Authors going to clear to {instance}: {', '.join([str(model.objects.get(pk=pk)) for pk in pk_set])}")
    elif action == 'post_clear':
        print(f"Authors cleared to {instance}: {', '.join([str(model.objects.get(pk=pk)) for pk in pk_set])}")


# custom signal
custom_signal = Signal()

@receiver(custom_signal)
def send_order_notification(sender, **kwargs):
    arg1_value = kwargs.get("arg1")
    arg2_value = kwargs.get("arg2")
    print(arg1_value,arg2_value,'from signal')


