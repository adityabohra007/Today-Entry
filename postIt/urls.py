from django.urls import path
from . import views


app_name='Post'
urlpatterns=[path('',views.PostIndexView.as_view(),name="index"),
			path('<int:pk>/',views.PostDetailView.as_view(),name="detail"),
			path('Show/',views.DatesIndexView.as_view(),name="dates"),
			path('Show/<int:pk>',views.DatesDetailsView.as_view(),name="datesdetails"),
             ]