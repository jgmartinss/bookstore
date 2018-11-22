from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = [
    path('sign_in/', views.SignInView.as_view(), name='sign-in'),
    path('sign_up/', views.SignUpView.as_view(), name='sign-up'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
