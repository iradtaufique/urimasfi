from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from urimasapp.render import Render
from urimasapp.models import Mission
from django.shortcuts import get_object_or_404




class Pdf(View):

    def get(self, request, pk):
        mission = get_object_or_404(Mission, pk=pk)
        params = {

            'invitation': mission,
            'request': request,
        }
        return Render.render('mission_pdf.html', params)








@login_required
def home(request):
    return render(request, 'home/home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



def profile(request):
    return render(request, 'profile.html')