from django.urls import path,include
from User.views import sampleview

urlpatterns = [
    path('view/',sampleview.as_view())
]