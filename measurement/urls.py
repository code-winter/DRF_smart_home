from django.urls import path

from measurement.views import SensorView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensor/<pk>', SensorDetailView.as_view()),
    path('sensor/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]