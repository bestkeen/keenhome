from django.shortcuts import render
import json
from users.models import User

# Create your views here.
def index(request):
	return render(request,'basemain.html')

def accounts_profile(request):
	if request.method == 'POST':
		a = json.loads(request.body.decode('utf-8'))
		b = User.objects.get(email = request.user.email)
		b.name = a['name']
		b.save()
		
	return render(request,'accounts_profile.html')