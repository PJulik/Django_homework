from django.urls import path
from .views import SensorView, SensorUpdate, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/<pk>/', MeasurementView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
 ]
