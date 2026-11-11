# Exercise 67 — Duck Typing
# Task: Create a notification system using duck typing.

# Requirements:
# 1. Create three independent classes:
# - Email
# - SMS
# - PushNotification
# 2. Each class must have a method called send(message).
# 3. Each method should display a different message indicating how the notification was sent.
# 4. Create one object from each class.
# 5. Store all three objects in a list.
# 6. Create a function called send_notification(notification, message) that calls the object's send() method.
# 7. Loop through the list and pass each object to that function.
# Rules:
# - No inheritance.
# - No common parent class.
# - All three classes must independently implement send().

class Email:

    def send(self, message):
        print(f"Received a {message} in Email.")


class SMS:

    def send(self, message):
        print(f"Received a {message} in SMS.")


class PushNotification:

    def send(self, message):
        print(f"Received a {message} in PushNotification.")

mail = Email()
sms = SMS()
pushnoty = PushNotification()

Types_of_messages = [mail, sms, pushnoty]

def send_notification(notification, message):
    notification.send(message)


for x in Types_of_messages:
    send_notification(x, "Hello! This is a notification")