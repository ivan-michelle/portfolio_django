from django.shortcuts import render, redirect
import Project.models as models
from Project.forms import ProjectForm
from django.urls import reverse

# Create your views here.
def portfolio(request):
    projects = models.Project.objects.all()
    return render(request, 'Project/portfolio.html', {'projects':projects})

def addproject(request):
    project_form = ProjectForm()

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            project = models.Project()
            project.title = request.POST.get('title')
            project.description = request.POST.get('description')
            project.image = project_form.cleaned_data['image']
            project.link = request.POST.get('link')
            project.save()
            
            return redirect(reverse('portfolio'))

    return render(request, 'project/addproject.html', {'project_add':project_form})    
