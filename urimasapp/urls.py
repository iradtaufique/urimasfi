from django.urls import path
from .views import urimasapp, member_staff, supervisor

urlpatterns = [

    path('', member_staff.MissionListView.as_view(), name='mission_request'),
    path('home/', urimasapp.home, name='home'),
    path('signup/', urimasapp.signup, name='signup'),
    path('staff_member/', member_staff.MissionListView.as_view(), name='mission_request'),
    path('mission/add/', member_staff.MissionCreateView.as_view(), name='mission_add'),

    path('report/', member_staff.Make_Report.as_view(), name='report'),



    path('invitation/<int:mission_id>/', supervisor.mission_details, name='invitation'),
    path('supervisor/', supervisor.MissionListView.as_view(), name='super_mission_list'),

    # path('school/', supervisor.SupervisorSchoolView.as_view(), name='student_interests'),

    path('approve/<int:mission_id>', supervisor.change_status, name='change_status'),
    path('rejected/<int:mission_id>', supervisor.reject_mission, name='reject_mission'),
    path('ajax/load-schools/', member_staff.load_schools, name='ajax_load_schools'),
    path('render/pdf/<int:pk>/', urimasapp.Pdf.as_view(), name='pdf'),
    path('profile/', urimasapp.profile, name='profile'),

]


