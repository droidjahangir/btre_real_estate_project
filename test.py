'''
from django.core.mail import send_mail

Send email
send_mail(
'Property Listing Inquiry',
'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
'traversy.brad@gmail.com',
[realtor_email, 'techguyinfo@gmail.com'],
fail_silently=False
)

send_mail(subject, message, from_email, recipient_list)
'''