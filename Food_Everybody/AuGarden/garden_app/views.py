from django.shortcuts import render
from garden_app.models import User

# Create your views here.
# This is the page that displays all the users as links
def users(request):
	all_users= User.objects.all()
	#A line of code here to go get all the users
	return render(request,'Show_Users.html',{'all_users':all_users})#Then I need a line of code to give the list of seekers to a template and render it.

