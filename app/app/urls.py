from datetime import datetime
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from authentication import views as viewHome
from authentication import forms, views
from catalog import views as catalogViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('authentication.urls')),
    path('prueba/',viewHome.prueba),
    path('employee_list/',catalogViews.employee_list),
    path('create_employee/',catalogViews.create_employee),
    path('update_employee/<id>',catalogViews.update_employee),
    path('',
         LoginView.as_view
         (
             template_name='login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
    path('login/',viewHome.login),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
]


if settings.DEBUG:
    urlpatterns += static(       settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
        
    urlpatterns += static( settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)

