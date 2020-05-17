from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import TransactionUpdateView, BudgetUpdateView, BudgetCreateView

urlpatterns = [
    path('', views.home),
    path('login', views.logIn),
    path('register', views.register),
    path('logout', views.logOut),

    path('dashboard', views.dashboard),
    path('manual', views.manual),
    path('transactions', views.transactions),
    path('charts', views.charts),
    path('bill', views.bill),
    path('transaction/<int:pk>/update', TransactionUpdateView.as_view(), name='transaction-update'),
    path('profile/update', views.ProfileUpdate, name='profile-update'),

    path('predict', views.handlePredict),
    path('csv', views.csvUpload),
    path('validate_username', views.validate_username),

    path('profile', views.profile),
    path('budget', views.BudgetPage),
    path('budget/<int:pk>/update', BudgetUpdateView.as_view(), name='budget-update'),
    path('budget/create', BudgetCreateView.as_view(), name='budget-create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
