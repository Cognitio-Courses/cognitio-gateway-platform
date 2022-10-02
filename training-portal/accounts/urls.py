from django.urls import path

from accounts.views import AccountLoginView, AccountLogoutView, AccountRegisterView, ContentCreatorAccountRegisterView, RedirectLoggedinAccountView

app_name = "account"

urlpatterns = [
    path('login', AccountLoginView.as_view(), name='login'),
    path('register', AccountRegisterView.as_view(), name='register'),
    path('register/content-creator', ContentCreatorAccountRegisterView.as_view(), name='register.content_creator'),
    path('redirect-authenticated', RedirectLoggedinAccountView.as_view(), name='redirect_authenticated_user'),
    path('logout', AccountLogoutView.as_view(), name='logout')
]
