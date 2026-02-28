from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    GalleryImage, Achievement, Award, CVContent, CVStatistics, CVEducation,
    CVCurrentPosition, CVExperience, CVProfessionalMembership, CVPublication,
    CVPatent, CVPersonalDetail, ProfileContent, PageView
)
from .forms import (
    LoginForm, GalleryImageForm, AchievementForm, AwardForm, 
    CVContentForm, ProfileContentForm
)

def home(request):
    try:
        profile = ProfileContent.objects.first()
    except:
        profile = None
    
    try:
        page_view = PageView.increment_view('home')
    except:
        page_view = None
    
    try:
        cv_stats = CVStatistics.objects.first()
    except:
        cv_stats = None
    
    return render(request, 'home.html', {'profile': profile, 'page_view': page_view, 'cv_stats': cv_stats})

def achievements(request):
    try:
        achievements = Achievement.objects.all()
    except:
        achievements = []
    return render(request, 'achievements.html', {'achievements': achievements})

def gallery(request):
    try:
        gallery_images = GalleryImage.objects.all()
    except:
        gallery_images = []
    return render(request, 'gallery.html', {'gallery_images': gallery_images})

def awards(request):
    try:
        awards = Award.objects.all()
    except:
        awards = []
    return render(request, 'awards.html', {'awards': awards})

def contact(request):
    return render(request, 'contact.html')

def cv(request):
    try:
        cv_files = CVContent.objects.all().order_by('-created_at')
    except:
        cv_files = []
    
    try:
        cv_stats = CVStatistics.objects.first()
    except:
        cv_stats = None
    
    try:
        cv_education = CVEducation.objects.all()
    except:
        cv_education = []
    
    try:
        cv_current_position = CVCurrentPosition.objects.all()
    except:
        cv_current_position = []
    
    try:
        cv_experience = CVExperience.objects.all()
    except:
        cv_experience = []
    
    try:
        cv_memberships = CVProfessionalMembership.objects.all()
    except:
        cv_memberships = []
    
    try:
        cv_publications = CVPublication.objects.all()
    except:
        cv_publications = []
    
    try:
        cv_patents = CVPatent.objects.all()
    except:
        cv_patents = []
    
    try:
        cv_personal_details = CVPersonalDetail.objects.all()
    except:
        cv_personal_details = []
    
    return render(request, 'cv.html', {
        'cv_files': cv_files,
        'cv_stats': cv_stats,
        'cv_education': cv_education,
        'cv_current_position': cv_current_position,
        'cv_experience': cv_experience,
        'cv_memberships': cv_memberships,
        'cv_publications': cv_publications,
        'cv_patents': cv_patents,
        'cv_personal_details': cv_personal_details
    })

# Admin Login
def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None and user.is_staff:
                login(request, user)
                messages.success(request, f'Welcome {username}!')
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Invalid credentials or insufficient permissions.')
    else:
        form = LoginForm()
    
    return render(request, 'admin_login.html', {'form': form})

def admin_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('admin_login')

@login_required(login_url='admin_login')
def admin_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, 'Access denied.')
        return redirect('home')
    
    try:
        gallery_count = GalleryImage.objects.count()
    except:
        gallery_count = 0
    
    try:
        achievement_count = Achievement.objects.count()
    except:
        achievement_count = 0
    
    try:
        award_count = Award.objects.count()
    except:
        award_count = 0
    
    context = {
        'gallery_count': gallery_count,
        'achievement_count': achievement_count,
        'award_count': award_count,
    }
    return render(request, 'admin_dashboard.html', context)

# Gallery Management
@login_required(login_url='admin_login')
def gallery_list(request):
    if not request.user.is_staff:
        return redirect('home')
    
    try:
        gallery_images = GalleryImage.objects.all()
    except:
        gallery_images = []
    return render(request, 'gallery_list.html', {'gallery_images': gallery_images})

@login_required(login_url='admin_login')
def gallery_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gallery image added successfully!')
            return redirect('gallery_list')
    else:
        form = GalleryImageForm()
    
    return render(request, 'gallery_form.html', {'form': form, 'title': 'Add Gallery Image'})

@login_required(login_url='admin_login')
def gallery_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    gallery = get_object_or_404(GalleryImage, pk=pk)
    
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gallery image updated successfully!')
            return redirect('gallery_list')
    else:
        form = GalleryImageForm(instance=gallery)
    
    return render(request, 'gallery_form.html', {'form': form, 'title': 'Edit Gallery Image'})

@login_required(login_url='admin_login')
def gallery_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    gallery = get_object_or_404(GalleryImage, pk=pk)
    gallery.delete()
    messages.success(request, 'Gallery image deleted successfully!')
    return redirect('gallery_list')

# Achievement Management
@login_required(login_url='admin_login')
def achievement_list(request):
    if not request.user.is_staff:
        return redirect('home')
    
    try:
        achievements = Achievement.objects.all()
    except:
        achievements = []
    return render(request, 'achievement_list.html', {'achievements': achievements})

@login_required(login_url='admin_login')
def achievement_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Achievement added successfully!')
            return redirect('achievement_list')
    else:
        form = AchievementForm()
    
    return render(request, 'achievement_form.html', {'form': form, 'title': 'Add Achievement'})

@login_required(login_url='admin_login')
def achievement_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    achievement = get_object_or_404(Achievement, pk=pk)
    
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            messages.success(request, 'Achievement updated successfully!')
            return redirect('achievement_list')
    else:
        form = AchievementForm(instance=achievement)
    
    return render(request, 'achievement_form.html', {'form': form, 'title': 'Edit Achievement'})

@login_required(login_url='admin_login')
def achievement_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    achievement = get_object_or_404(Achievement, pk=pk)
    achievement.delete()
    messages.success(request, 'Achievement deleted successfully!')
    return redirect('achievement_list')

# Award Management
@login_required(login_url='admin_login')
def award_list(request):
    if not request.user.is_staff:
        return redirect('home')
    
    try:
        awards = Award.objects.all()
    except:
        awards = []
    return render(request, 'award_list.html', {'awards': awards})

@login_required(login_url='admin_login')
def award_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Award added successfully!')
            return redirect('award_list')
    else:
        form = AwardForm()
    
    return render(request, 'award_form.html', {'form': form, 'title': 'Add Award'})

@login_required(login_url='admin_login')
def award_edit(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    award = get_object_or_404(Award, pk=pk)
    
    if request.method == 'POST':
        form = AwardForm(request.POST, request.FILES, instance=award)
        if form.is_valid():
            form.save()
            messages.success(request, 'Award updated successfully!')
            return redirect('award_list')
    else:
        form = AwardForm(instance=award)
    
    return render(request, 'award_form.html', {'form': form, 'title': 'Edit Award'})

@login_required(login_url='admin_login')
def award_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    award = get_object_or_404(Award, pk=pk)
    award.delete()
    messages.success(request, 'Award deleted successfully!')
    return redirect('award_list')

# CV Management
@login_required(login_url='admin_login')
def cv_list(request):
    if not request.user.is_staff:
        return redirect('home')
    
    try:
        cv_files = CVContent.objects.all()
    except:
        cv_files = []
    return render(request, 'cv_list.html', {'cv_files': cv_files})

@login_required(login_url='admin_login')
def cv_add(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method == 'POST':
        form = CVContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'CV added successfully!')
            return redirect('cv_list')
    else:
        form = CVContentForm()
    
    return render(request, 'cv_form.html', {'form': form, 'title': 'Add CV'})

@login_required(login_url='admin_login')
def cv_delete(request, pk):
    if not request.user.is_staff:
        return redirect('home')
    
    cv = get_object_or_404(CVContent, pk=pk)
    cv.delete()
    messages.success(request, 'CV deleted successfully!')
    return redirect('cv_list')

# Profile Management
@login_required(login_url='admin_login')
def profile_edit(request):
    if not request.user.is_staff:
        return redirect('home')
    
    profile, created = ProfileContent.objects.get_or_create(pk=1)
    
    if request.method == 'POST':
        form = ProfileContentForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('admin_dashboard')
    else:
        form = ProfileContentForm(instance=profile)
    
    return render(request, 'profile_form.html', {'form': form, 'title': 'Edit Profile'})
