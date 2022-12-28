from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('submitData', views.PeakView)


router = routers.DefaultRouter()
router.register('GET /submitData/<id>', views.PeakView)

router = routers.DefaultRouter()
router.register('PATCH /submitData/<id>', views.PeakView)

router = routers.DefaultRouter()
router.register('GET /submitData/?user__email=<email> ', views.PeakView)

urlpatterns = [
    path('', include(router.urls)),
    # path('create/', views.CreatePostAPIView.as_view(),name='post_create'),
    # path('update/<int:pk>/',views.UpdatePostAPIView.as_view(),name='update_post'),
    # path('delete/<int:pk>/',views.DeletePostAPIView.as_view(),name='delete_post')
]