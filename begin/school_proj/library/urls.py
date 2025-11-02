from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.list, name='list'),
    path('lg', views.log, name='log'),
    path('book/<int:book_id>/', views.det, name='det'),
    path('per', views.helper, name='helper'),
    path('reg', views.RegisterView.as_view(), name='register'),
    path('log', views.LoginView.as_view(), name='login'),
    path('prof', views.ProfileView.as_view(), name='profile'),
    path('book/<int:book_id>/reserve/', views.reserve_book, name='reserve_book'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
