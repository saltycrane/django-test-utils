import django.dispatch

pre_request =  django.dispatch.Signal(providing_args=['url', 'request'])
post_request =  django.dispatch.Signal(providing_args=['url', 'response'])
start_run =  django.dispatch.Signal()
finish_run =  django.dispatch.Signal()
