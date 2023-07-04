from django.urls import path
from .views import form_submission

urlpatterns = [
    path('', form_submission, name='form_submission'),
    # Other URL patterns
]
