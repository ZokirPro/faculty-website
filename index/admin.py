from django.contrib import admin
from .models import *
from parler.admin import TranslatableAdmin
# Register your models here.


@admin.register(MainInfos)
class MainInfosAdmin(TranslatableAdmin):
    fieldsets = (
		('Veb sahifaning asosiy malumotlari', {'fields': ['logo','phone','email','address',"map_url",'telegram','instagram','facebook']}),
	)


@admin.register(TalentedStudents)
class TalentedStudentsAdmin(TranslatableAdmin):
    list_display = ('fullname','specialization')

# @admin.register(CategoryTexts)
# class CategoryTextsAdmin(TranslatableAdmin):
#     list_display = ('name',)

@admin.register(Texts)
class TextsAdmin(TranslatableAdmin):
    list_display = ('category',)



@admin.register(ReceptionTimes)
class ReceptionTimesAdmin(TranslatableAdmin):
    list_display = ('employee','room','startTime','endTime')

@admin.register(IndexCarousel)
class IndexCarouselAdmin(TranslatableAdmin):
    list_display = ('title','text')


@admin.register(News)
class NewsAdmin(TranslatableAdmin):
    list_display = ('title','category')
    fieldsets = (
		('Yangiliklar', {'fields': ['title','short_description','full_desc','category','image',]}),
	)

@admin.register(Resources)
class ResourcesAdmin(TranslatableAdmin):
    list_display = ('title','category')
    fieldsets = (
		('Qonunlar', {'fields': ['title','short_description','file','image',"category"]}),
	)


@admin.register(ResourceCategory)
class ResourceCategoryAdmin(TranslatableAdmin):
    list_display = ('name',)

@admin.register(Employees)
class EmployeesAdmin(TranslatableAdmin):
    list_display = ('name',)


@admin.register(CategoryTexts)
class DepartMentsTextAdmin(TranslatableAdmin):
    list_display = ('name',)


