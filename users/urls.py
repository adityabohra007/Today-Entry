from django.urls import path
from . import views

app_name="users"
urlpatterns=[  path('signup/', views.SignUp.as_view(), name='signup'),
			path('',views.PostIndexView.as_view(),name="index"),
			path('<int:pk>/',views.PostDetailView.as_view(),name="detail"),
			path('Show/',views.DatesIndexView.as_view(),name="dates"),
			path('Show/<int:pk>',views.DatesDetailsView.as_view(),name="datesdetails"),
			path('inputForm',views.PostFormView.as_view()),
			path('category/<int:pk>/',views.CategoryView.as_view(),name="category"),
			#path('Add/',views.get_name,name="form"),
			#path('category/',views.categoryListView.as_view(),name="cat"),
			
             ]