from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def send_mail_page(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                messages.success(request, 'Email sent successfully!')
            except Exception as e:
                messages.error(request, f'Error sending email: {e}')
        else:
            messages.error(request, 'All fields are required')

    return render(request, 'index.html')
