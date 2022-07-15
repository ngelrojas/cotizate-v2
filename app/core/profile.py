from django.db import models
from .abstract import AbstractProfile
from .user import User
from .country import Country
from .city import City


def nameFile(instance, filename):
    """save images in personal folder"""
    fdir = str(instance).replace(" ", "_")
    return "/".join(["images/profiles/personal", fdir, filename])


class PersonalProfile(AbstractProfile):
    """personal profile"""

    current_position = models.CharField(max_length=50, blank=True, null=True)
    headline = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to=nameFile, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

    @classmethod
    def get_all(cls, request):
        return cls.objects.filter(user=request.user, delete=False)

    @classmethod
    def get_by_id(cls, request, pk, delete=False):
        return cls.objects.get(id=pk, user=request.user, delete=delete)

    @classmethod
    def created(cls, request):
        created = cls.objects.create(
            cinit = request.data.get("cinit"), 
            address = request.data.get("address"),
            number_address = request.data.get("number_address"), 
            neightbordhood = request.data.get("neightbordhood"), 
            cellphone = requests.data.get("cellphone"), 
            telephone = request.data.get("telephone"), 
            description = request.data.get("description"), 
            rs_facebook = request.data.get("rs_facebook"), 
            rs_twitter = request.data.get("rs_twitter"), 
            rs_linkedin = request.data.get("rs_linkedin"), 
            rs_another = request.data.get("rs_another"), 
            current_position = request.data.get("current_position"), 
            headline = request.data.get("headline"), 
            birthdate = request.data.get("birthdate"), 
            photo = request.data["photo"], 
            user = request.user, 
            countries = request.data.get("country_id"), 
            cities = request.data.get("city_id") 
        )
        return created.id

    @classmethod
    def updated(cls, request, pk):
        data = cls.get_by_id(request, pk) 
        data.cinit = request.data.get("cinit"), 
        data.address = request.data.get("address"),
        data.number_address = request.data.get("number_address"), 
        data.neightbordhood = request.data.get("neightbordhood"), 
        data.cellphone = requests.data.get("cellphone"), 
        data.telephone = request.data.get("telephone"), 
        data.description = request.data.get("description"), 
        data.rs_facebook = request.data.get("rs_facebook"), 
        data.rs_twitter = request.data.get("rs_twitter"), 
        data.rs_linkedin = request.data.get("rs_linkedin"), 
        data.rs_another = request.data.get("rs_another"), 
        data.current_position = request.data.get("current_position"), 
        data.headline = request.data.get("headline"), 
        data.birthdate = request.data.get("birthdate"), 
        if request.data["photo"]:
            data.photo = request.data["photo"], 
        data.countries = request.data.get("country_id"), 
        data.cities = request.data.get("city_id")
        data.save()
        return data.id

    @classmethod
    def erase(cls, request, pk):
        data = cls.get_by_id(request, pk)
        data.delete = True
        data.save()
        return True
    


