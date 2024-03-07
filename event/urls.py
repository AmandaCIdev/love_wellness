from django.urls import path

from . import views

urlpatterns = [
    path('', views.EventList.as_view(), name = 'home'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),
=======
>>>>>>> c96785c (register, signin, signout, basic styling, change title and head/logo, connect home and about, js file for reviews, event_detail.html creation, add functions to event views)
=======
    path('<slug:slug>/', views.event_detail, name='event_detail'),
>>>>>>> 0b5bb30 (event appears, review delete now works, event_detail works)
]