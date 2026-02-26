from django.db import models
from django.contrib.auth.models import User

class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Award(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(null=True, blank=True)
    certificate = models.FileField(upload_to='awards/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CVContent(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='cv/')
    version = models.CharField(max_length=50, default='1.0')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.version}"


class CVStatistics(models.Model):
    google_scholar_citations = models.CharField(max_length=50, default='239+')
    h_index = models.CharField(max_length=50, default='H-8')
    publications = models.CharField(max_length=50, default='50+')
    patents = models.CharField(max_length=50, default='9+')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Statistics"

    def __str__(self):
        return "CV Statistics"


class CVEducation(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    year = models.CharField(max_length=100)
    specialization = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "CV Education"

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class CVCurrentPosition(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    from_date = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Current Position"
        ordering = ['order']

    def __str__(self):
        return self.title


class CVExperience(models.Model):
    position = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    from_date = models.CharField(max_length=100)
    to_date = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Experience"
        ordering = ['order']

    def __str__(self):
        return f"{self.position} at {self.institution}"


class CVProfessionalMembership(models.Model):
    organization = models.CharField(max_length=200)
    membership_type = models.CharField(max_length=200)
    from_date = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Professional Memberships"
        ordering = ['order']

    def __str__(self):
        return f"{self.membership_type} - {self.organization}"


class CVPublication(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=500)
    journal = models.CharField(max_length=300)
    year = models.CharField(max_length=10)
    doi = models.CharField(max_length=100, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Publications"
        ordering = ['-year', 'order']

    def __str__(self):
        return f"{self.title} ({self.year})"


class CVPatent(models.Model):
    title = models.CharField(max_length=300)
    patent_number = models.CharField(max_length=100, null=True, blank=True)
    filing_date = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=[
        ('filed', 'Filed'),
        ('pending', 'Pending'),
        ('granted', 'Granted')
    ], default='filed')
    description = models.TextField()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Patents"
        ordering = ['order']

    def __str__(self):
        return self.title


class CVPersonalDetail(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=500)
    order = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "CV Personal Details"
        ordering = ['order']

    def __str__(self):
        return f"{self.key}: {self.value}"


class ProfileContent(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Profile Content"

    def __str__(self):
        return self.name


class PageView(models.Model):
    page_name = models.CharField(max_length=100, unique=True, default='home')
    view_count = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Page Views"

    def __str__(self):
        return f"{self.page_name} - {self.view_count} views"

    @classmethod
    def increment_view(cls, page_name='home'):
        obj, created = cls.objects.get_or_create(page_name=page_name)
        obj.view_count += 1
        obj.save()
        return obj
