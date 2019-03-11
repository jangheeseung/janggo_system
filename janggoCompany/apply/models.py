from django.db import models

# Create your models here.
TYPE_CHOICES = (
        ('intern','intern'),
        ('employee','employee')
    )

class Hire(models.Model):
    kind = models.CharField(max_length=125)
    num = models.IntegerField()
    hire_type = models.CharField(max_length=125, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    content1 = models.TextField()
    content2 = models.TextField()

    def __str__(self):
        return self.kind
    
    def summary(self):
        return self.kind[:20]

class Apply(models.Model):
    name = models.CharField(max_length=125, blank=True, null=True)
    age = models.IntegerField()
    phone = models.CharField(max_length=125, blank=True, null=True)
    e_mail = models.CharField(max_length=125, blank=True, null=True)
    address = models.CharField(max_length=125, blank=True, null=True)
    password = models.CharField(max_length=125, blank=True, null=True)
    
    college = models.CharField(max_length=125, blank=True, null=True)
    major = models.CharField(max_length=125, blank=True, null=True)
    graduate = models.BooleanField(default=False)

    document = models.FileField(upload_to='documents/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    hire = models.ForeignKey(Hire, on_delete = models.CASCADE)
    
    # 업로드된 파일과 객체를 삭제하는 메서드
    def delete(self, *args, **kwargs):
        self.document.delete()
        self.filtered_document.delete()
        super(Apply, self).delete(*args, **kwargs)

    def __str__(self):
        return self.name