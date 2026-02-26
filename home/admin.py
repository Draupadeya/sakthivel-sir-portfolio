from django.contrib import admin
from .models import (
    GalleryImage, Achievement, Award, CVContent, CVStatistics, CVEducation,
    CVCurrentPosition, CVExperience, CVProfessionalMembership, CVPublication,
    CVPatent, CVPersonalDetail, ProfileContent, PageView
)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    ordering = ('order',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('date',)

@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'date', 'created_at')
    search_fields = ('title', 'organization', 'description')
    list_filter = ('date', 'organization')

@admin.register(CVContent)
class CVContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'version', 'created_at')
    search_fields = ('title', 'version')
    list_filter = ('created_at',)

@admin.register(CVStatistics)
class CVStatisticsAdmin(admin.ModelAdmin):
    list_display = ('google_scholar_citations', 'h_index', 'publications', 'patents')

@admin.register(CVEducation)
class CVEducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'year', 'specialization', 'order')
    list_editable = ('order',)
    search_fields = ('degree', 'institution', 'specialization')
    ordering = ('order',)

@admin.register(CVCurrentPosition)
class CVCurrentPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'institution', 'from_date')
    search_fields = ('title', 'department', 'institution')

@admin.register(CVExperience)
class CVExperienceAdmin(admin.ModelAdmin):
    list_display = ('position', 'institution', 'from_date', 'to_date', 'order')
    list_editable = ('order',)
    search_fields = ('position', 'institution')
    ordering = ('order',)

@admin.register(CVProfessionalMembership)
class CVProfessionalMembershipAdmin(admin.ModelAdmin):
    list_display = ('organization', 'membership_type', 'from_date', 'order')
    list_editable = ('order',)
    search_fields = ('organization', 'membership_type')
    ordering = ('order',)

@admin.register(CVPublication)
class CVPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'journal', 'year', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'journal', 'authors')
    list_filter = ('year',)
    ordering = ('-year', 'order')

@admin.register(CVPatent)
class CVPatentAdmin(admin.ModelAdmin):
    list_display = ('title', 'patent_number', 'status', 'filing_date', 'order')
    list_editable = ('order',)
    search_fields = ('title', 'patent_number')
    list_filter = ('status',)
    ordering = ('order',)

@admin.register(CVPersonalDetail)
class CVPersonalDetailAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'order')
    list_editable = ('order',)
    search_fields = ('key', 'value')
    ordering = ('order',)

@admin.register(ProfileContent)
class ProfileContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'department', 'updated_at')
    search_fields = ('name', 'title', 'department')
@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'view_count', 'last_updated')
    readonly_fields = ('page_name', 'view_count', 'last_updated')
    
    def has_add_permission(self, request):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False