from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Projects
    path('todo/', views.todo, name='todo'),
    path('cursor/', views.cursor, name='cursor'),
    path('calculator/', views.calculator, name='calculator'),
    path('musicplayer/', views.musicplayer, name='musicplayer'),
    path('weather/', views.weather, name='weather'),
    path('colourchange/', views.colourchange, name='colourchange'),
    path('expensetracker/', views.expensetracker, name='expensetracker'),
    path('passwordgenerator/', views.passwordgenerator, name='passwordgenerator'),
    path('profile/', views.profile_view, name='profile'),


    # UI and Contact
    path('navbar/', views.navbar, name='navbar'),
    path('contact/', views.contact, name='contact'),

    # Auth
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    # Live reload
    path("__reload__/", include("django_browser_reload.urls")),
]
