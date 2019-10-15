from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView
from urimasapp.models import User, Mission, Report, Supervisor, School
from urimasapp.forms import StaffSignUpForm, MissionForm
from django.contrib.auth.decorators import login_required




class StaffSignUpView(CreateView):
    model = User
    form_class = StaffSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()

        return redirect('login')



@method_decorator(login_required, name='dispatch')
class MissionListView(ListView):
    model = Mission
    ordering = ('mission_purpose', )
    context_object_name = 'missions'
    template_name = 'urimasapp/staff_mission_list.html'

    def get_queryset(self):
        queryset = self.request.user.missions \
            .select_related('school') \

        return queryset



class MissionCreateView(CreateView):
    model = Mission
    form_class = MissionForm

    template_name = 'urimasapp/mission_add_form.html'

    def form_valid(self, form):
        mission = form.save(commit=False)
        mission.owner = self.request.user
        mission.save()
        messages.success(self.request, 'The mission was requested successfully!.')
        return redirect('mission_request')

def load_schools(request):
    category_id = request.GET.get('category')
    schools = School.objects.filter(category_id=category_id).order_by('name')

    return render(request, 'urimasapp/dropdown.html', {'schools': schools})




class Make_Report(CreateView):
    model = Report
    fields = ('file', 'note')

    template_name = 'urimasapp/report.html'


    def form_valid(self, form):
        report = form.save(commit=False)
        report.owner = self.request.user
        report.save()
        messages.success(self.request, 'The mission was requested successfully!.')
        return redirect('mission_request')