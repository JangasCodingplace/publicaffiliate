from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name="index"),
     path('android-01/<slug:key>',
          views.redirect_fallback_url,
          name="AndroidRedirect"),
     path('ios-01/<slug:key>',
          views.redirect_ios_countdown,
          name="IOSCountdown"),
     path('ios-02/<slug:key>',
          views.ios_urlgenius,
          name="IOSURLGenius"),
     path('ios-02/<slug:key>',
          views.twago,
          name="Twago"),
]
