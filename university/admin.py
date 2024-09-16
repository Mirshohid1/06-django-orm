from django.contrib import admin
from .models import Teacher, Subject, Kafedra, Student, Group, Faculty

class SubjectInline(admin.TabularInline):
    model = Subject
    extra = 1

class KafedraInline(admin.TabularInline):
    model = Kafedra
    extra = 1

class GroupInline(admin.TabularInline):
    model = Group
    extra = 1

class FacultyInline(admin.TabularInline):
    model = Faculty
    extra = 1

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [SubjectInline]
    list_display = ('first_name', 'last_name')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    inlines = [KafedraInline]
    list_display = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [KafedraInline, GroupInline]
    list_display = ('first_name', 'last_name')
    
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [FacultyInline]
    list_display = ('name',)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', )