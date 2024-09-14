from django.urls import include, path

from .views import EventsView, EventView, RegistrationOnEvent, RegisterView, LoginView



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('events/', EventsView.as_view(), name='event-list'),
    path('events/<int:event_id>/registration/', RegistrationOnEvent.as_view(), name='event-registration'),
    path('events/<int:event_id>/', EventView.as_view(), name='event-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]