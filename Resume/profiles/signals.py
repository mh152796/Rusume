from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf import settings
from .models import Profile
from cv.models import ResumeModel


# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
       user = instance
       profile = Profile.objects.create(
           user = user,
           username = user.username,
           phone = user.phone,
           name = user.first_name + user.last_name,
           address = user.address,
           email = user.email,
           first_name = user.first_name,
           last_name = user.last_name,
       )
       
       subject = 'Welcome To CV World'
       message = 'We are glad you are here!'
       
       send_mail(
           subject,
           message,
           settings.EMAIL_HOST_USER,
           [profile.email],
           fail_silently=False,
       )

# def createCv(sender, instance, created, **kwargs):
#     if created:
#        profiles = instance
#        profile = ResumeModel.objects.create(
#            profiles = profiles,
#            name = profiles.first_name + profiles.last_name,
#            phone = profiles.phone,
#            address = profiles.address
#        )

def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.username = profile.username
        user.phone = profile.phone
        user.address = profile.address
        user.email = profile.email
        user.save()
    

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
# post_save.connect(createCv, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)