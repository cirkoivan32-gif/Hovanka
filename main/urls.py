from django.urls import path

from .views import (
    base_checkout_redirect,
    control_panel,
    dashboard,
    home,
    join_pro_waitlist,
    login_view,
    logout_view,
    register_view,
)


urlpatterns = [
    path("", home, name="home"),
    path("accounts/register/", register_view, name="register"),
    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    path("app/", dashboard, name="dashboard"),
    path("waitlist/pro/", join_pro_waitlist, name="join-pro-waitlist"),
    path("checkout/base/", base_checkout_redirect, name="base-checkout"),
    path("ops/", control_panel, name="control"),
]
