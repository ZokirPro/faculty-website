from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import CharField, DateTimeField
from phonenumber_field.modelfields import PhoneNumberField
from parler.models import TranslatableModel, TranslatedFields
from django.core.validators import RegexValidator
# Create your models here.


class MainInfos(TranslatableModel):
    translations = TranslatedFields(
        address = models.CharField(("Manzil"), max_length=200)
    )
    logo = models.ImageField(("Logo"))
    email = models.EmailField(("Email"), max_length=254)
    phone = PhoneNumberField('Telefon raqam')
    telegram = models.URLField(("Telegramga havola"), max_length=200,blank=True)
    instagram = models.URLField(("Instagramga link"), max_length=200,blank=True)
    facebook = models.URLField(("Facebook ga link"), max_length=200,blank=True)
    youtube = models.URLField(("Facebook ga link"), max_length=200,blank=True)
    map_url = models.URLField("Google yoki yandex xaritaga link")
    
    class Meta:
        verbose_name = ("Asosiy malumotlar ")
        verbose_name_plural = ("Asosiy malumotlar ")

    def __str__(self):
        return "Asosiy malumotlar"


EmployeesEducationTitles = [
    ("Stajor_oqituvchi","Stajor 'oqituvchi"),
    ("oqituvchi","O'qituvchi"),
    ("katta_oqituvchi","Katta o'qituvchi"),
    ("dotsent","Dotsent"),
    ("professor","Professor"),
    ("akademik","Akademik")
]



class Employees(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(("FIO"), max_length=200),
        position = models.CharField(("Mansabi"), max_length=200)
        
    )
    educationTitle=models.CharField("O'qitish Mansabi",max_length=50,choices=EmployeesEducationTitles)
    birthdate = models.DateField("Tugilgan yili")
    passportSeries = models.CharField(
        "Passport seriyasi",
        max_length=2,
        validators=[
            RegexValidator(
                regex="[a-zA-Z]",
                message="Notogri passport seriyasi",
                code="invalid_passportSeries"
            )
        ]
    )
    passportNumber = models.CharField(max_length=7,validators=[
        RegexValidator(
            regex="[0-9]{7}",
            code="invalid_passportNumber",
            message="Notogri passport nomer"
            
        )
    ])
    email=models.EmailField("Email")
    dateOfEntry = models.DateField("Ish boshlagan vaqti")
    image = models.ImageField(("Rasmi"))

    class Meta:
        verbose_name = ("Xodimlar ")
        verbose_name_plural = ("Xodimlar ")

    def __str__(self):
        return self.name


class ReceptionTimes(TranslatableModel):
    translations = TranslatedFields(
        room =models.CharField(("Xona raqami"), max_length=15)
    )
    employee = models.ForeignKey("Employees", verbose_name=("Xodim"), on_delete=models.CASCADE)
    startTime = models.TimeField(("Qabul qilish boshlanish vaqti"))
    endTime = models.TimeField(("Qabul qilish tugash vaqti"))
    
    

    class Meta:
        verbose_name = ("Qabul qiluvchi odamlar ")
        verbose_name_plural = ("Qabul qiluvchi odamlar ")

    def __str__(self):
        return f'{self.employee.name} {self.startTime}-{self.endTime}'




class IndexCarousel(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(("Sarlavhasi"), max_length=200),
        text = models.CharField(("Slayd matni"),max_length=10000000),
    )
    image = models.ImageField(("Slayd Rasmi"))
    

    class Meta:
        verbose_name = ("Slaydlar ")
        verbose_name_plural = ("Slaydlar ")

    def __str__(self):
        return self.title


NEWS_TYPE = [
    ('1', "Tanlo'v yangiliklari"),
    ('2', 'Talim yangiliklari'),
]


class News(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(("Yangilik sarlavhasi"), max_length=200),
        short_description = models.CharField(("Yangilik qisqa tavsifi"),max_length=200),
        full_desc = RichTextUploadingField("To'liq tavsif"),
        
    )
    category = models.CharField(("Kategoriyasi"),choices=NEWS_TYPE ,max_length=50)
    image = models.ImageField(("Rasm"))
    createdDate = models.DateTimeField('Yaratilgan vaqti',auto_now_add=True)

    class Meta:
        verbose_name = ("Yangiliklar ")
        verbose_name_plural = ("Yangiliklar ")

    def __str__(self):
        return self.title


class ResourceCategory(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(("Nomi"), max_length=50)
    )
    class Meta:
        verbose_name = ("Resurs kategoriyalari ")
        verbose_name_plural = ("Resurs kategoriyalari  ")

    def __str__(self):
        return self.name


class Resources(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(("Qonun sarlavhasi"), max_length=200),
        short_description = models.TextField(("Qonun qisqa tavsifi"),max_length=200),
        file = models.FileField(("Fayl")),
        
    )
    category = models.ForeignKey(ResourceCategory, verbose_name=("Resurs kategoriyasi"), on_delete=models.CASCADE)
    createdDate = models.DateTimeField('Yaratilgan vaqti',auto_now_add=True)
    image = models.ImageField(("Rasm"))
    

    class Meta:
        verbose_name = ("Resurslar ")
        verbose_name_plural = ("Resurslar ")

    def __str__(self):
        return self.title



class TalentedStudents(TranslatableModel):
    translations = TranslatedFields(
        fullname = models.CharField("To'liq ismi",max_length=100),
        address = models.CharField("Address",max_length=200),
        desc = RichTextUploadingField("To'liq tavsif"),
        title = models.CharField("Ilmiy unvoni",max_length=100),
        specialization = models.CharField("Mutaxasisligi",max_length=100)
    )
    birthdate = models.DateField(("Tug'ilgan kuni"))
    img = models.ImageField(("Rasm"))
    isInHome = models.BooleanField("Bosh sahifada tursinmi")

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = ("Talantli fakultet yulduzlar")
        verbose_name_plural = ("Talantli fakultet yulduzlar ")


class CategoryTexts(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField("Nomi",max_length=100)
    )

    class Meta:
        verbose_name = ("Tekst kategoriyalari ")
        verbose_name_plural = ("Tekst kategoriyalari ")

    def __str__(self):
        return self.name
    


class Texts(TranslatableModel):
    translations = TranslatedFields(
        desc = RichTextUploadingField("Tekst")
    )
    category = models.OneToOneField(CategoryTexts,on_delete=models.CASCADE)


    def __str__(self):
        return self.category.name
        
    class Meta:
        verbose_name = ("Tekstlar")
        verbose_name_plural = ("Tekstlar")
