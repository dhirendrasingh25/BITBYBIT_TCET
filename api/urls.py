from django.urls import path

from . import views

def dummy_head_view(request):
    return HttpResponse(status=200)
    
urlpatterns = [
    path('api/register/', views.register_view, name='register'),
    path('api/login/', views.login_view, name='api-login'),
    path('api/logout/', views.logout_view, name='api-logout'),
    path('api/session/', views.session_view, name='api-session'),
    path('api/whoami/', views.whoami_view, name='api-whoami'),
]