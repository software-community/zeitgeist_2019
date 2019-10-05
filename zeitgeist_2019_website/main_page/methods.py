from instamojo_wrapper import Instamojo
import os
from fcm_django.models import FCMDevice


def payment_request(name, amount, purpose, email, mobile):
    api = Instamojo(api_key=os.getenv('api_auth_key'),
                    auth_token=os.getenv('api_auth_token'))

    # Create a new Payment Request
    response = api.payment_request_create(
        buyer_name=name,
        amount=amount,
        purpose=purpose,
        send_email=True,
        email=email,
        phone=mobile,
        redirect_url="https://zeitgeist.org.in/payment_redirect/",
        webhook="https://zeitgeist.org.in/webhook/"
    )
    return response


def accomodation_payment_request(name, amount, purpose, email, mobile):
    api = Instamojo(api_key=os.getenv('api_auth_key'),
                    auth_token=os.getenv('api_auth_token'))

    # Create a new Payment Request
    response = api.payment_request_create(
        buyer_name=name,
        amount=amount,
        purpose=purpose,
        send_email=True,
        email=email,
        phone=mobile,
        redirect_url="https://zeitgeist.org.in/accomodation_payment_redirect/",
        webhook="https://zeitgeist.org.in/accomodation_weebhook/"
    )
    return response


def support_payment_request(name, amount, purpose, email, mobile):
    api = Instamojo(api_key=os.getenv('api_auth_key'),
                    auth_token=os.getenv('api_auth_token'))

    # Create a new Payment Request
    response = api.payment_request_create(
        buyer_name=name,
        amount=amount,
        purpose=purpose,
        send_email=True,
        email=email,
        phone=mobile,
        redirect_url="https://zeitgeist.org.in/support_payment_redirect/",
        webhook="https://zeitgeist.org.in/support_weebhook/"
    )
    return response

def sendNotification(title, message):
    devices = FCMDevice.objects.all()
    devices.send_message(title=title, body=message, data={"click_action": "FLUTTER_NOTIFICATION_CLICK"})
