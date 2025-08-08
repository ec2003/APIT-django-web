from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import UserProject
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def project_list(request):
    # This view will render the list of projects for the logged-in user
    projects = UserProject.objects.filter(user=request.user)
    context = {
        'projects': projects
    }
    return render(request, 'project/project_list.html', context)

@login_required
def project_add(request):
    # This view will handle adding a new project
    if request.method == 'POST':
        # Handle form submission for adding a project
        project_name = request.POST.get('project_name')
        description = request.POST.get('description', '')
        user = request.user

        # Create a new project instance and save it to the database
        if not project_name:
            messages.error(request, "Project name is required.")
            return render(request, 'project/project_add.html')
        
        if UserProject.objects.filter(user=user, project_name=project_name).exists():
            messages.error(request, "Project with this name already exists.")
            return render(request, 'project/project_add.html')
        
        project = UserProject(user=user, project_name=project_name, description=description)
        project.save()
        messages.success(request, "Project added successfully.")
        return redirect(reverse('project_detail_by_uuid', kwargs={'project_uuid': project.uuid}))
    else:
        # Render the project add form
        return render(request, 'project/project_add.html')

@login_required
def project_detail_by_uuid(request, project_uuid):
    # Use get_object_or_404 to retrieve the object or raise a 404 error if not found
    project = get_object_or_404(UserProject, uuid=project_uuid)

    context = {
        'project': project
    }
    return render(request, 'project/project_view.html', context)

@login_required
def project_edit(request, project_uuid):
    # This view will handle editing an existing project
    project = get_object_or_404(UserProject, uuid=project_uuid, user=request.user)

    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        description = request.POST.get('description', '')

        if not project_name:
            messages.error(request, "Project name is required.")
            return render(request, 'project/project_edit.html', {'project': project})

        # Update the project instance and save it to the database
        project.project_name = project_name
        project.description = description
        project.save()
        messages.success(request, "Project updated successfully.")
        return redirect(reverse('project_detail_by_uuid', kwargs={'project_uuid': project.uuid}))
    
    return render(request, 'project/project_edit.html', {'project': project})

@login_required
def project_delete(request, project_uuid):
    # This view will handle deleting an existing project
    project = get_object_or_404(UserProject, uuid=project_uuid, user=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project deleted successfully.")
        return redirect('project_list')
    return render(request, 'project/project_delete.html', {'project': project})