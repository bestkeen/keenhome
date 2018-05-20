from django.shortcuts import render
import json
from users.models import User

# Create your views here.
def index(request):
	return render(request,'basemain.html')

def get_data():
	reader = []
	for line in open('/home/keen/bigfile.txt','r',encoding="utf-8"):
		reader.append(line)
	return reader

def stock(request):
	data = get_data()
	return render(request,'stock.html',{'data':data})

def accounts_profile(request):
	if request.method == 'POST':
		a = json.loads(request.body.decode('utf-8'))
		b = User.objects.get(email = request.user.email)
		b.name = a['name']
		b.save()
	return render(request,'accounts_profile.html')

#if __name__ == "__main__":
#	print (get_data())
