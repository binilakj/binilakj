from django . urls import path
from . import views

app_name = 'FWapp'
urlpatterns = [
    path('', views.procat, name='procat'),
    path('<slug:catslug>/', views.procat, name='products_by_category'),
    path('<slug:catslug>/<slug:proslug>/', views.prodeta, name='procatdet')
]
