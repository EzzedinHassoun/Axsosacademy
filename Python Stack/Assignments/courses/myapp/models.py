from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def create_course(post):
        return Course.objects.create(name=post['name'],description=post['description'])
    
    def get_courses():
        return Course.objects.all()
    
    def get_course_info(courseid):
        return Course.objects.get(id=courseid)
    
    def delete_course(courseid):
        deleted_course=Course.objects.get(id=courseid)
        deleted_course.delete()
        return