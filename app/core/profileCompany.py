from django.db import models
from .abstract import AbstractProfile
from .country import Country
from .city import City
from .user import User


def nameFile(instance, filename):
    fdir = str(instance).replace(" ", "_")
    return "/".join(["images/profiles/company", fdir, filename])


class ProfileCompany(AbstractProfile):
    """profile company"""

    TYPE_INST = ((1, "COMPANY"), (2, "ASSOCIATION"), (3, "ANOTHER"))

    company_name = models.CharField(max_length=100, blank=True, null=True)
    representative = models.BooleanField(default=False)
    heading = models.CharField(max_length=50, blank=True, null=True)
    email_company = models.EmailField(max_length=250, blank=True, null=True)
    photo = models.ImageField(upload_to=nameFile, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    countries = models.ForeignKey(Country, on_delete=models.CASCADE)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)
    institution_type = models.PositiveSmallIntegerField(choices=TYPE_INST, default=1)

    def __str__(self):
        return self.company_name

    @classmethod
    def created(cls, request, country, city):
        res = cls.objects.create(
            cinit = request.data.get("cinit"), 
            address = request.data.get("address"),
            number_address = request.data.get("number_address"), 
            neightbordhood = request.data.get("neightbordhood"), 
            cellphone = request.data.get("cellphone"), 
            telephone = request.data.get("telephone"), 
            description = request.data.get("description"), 
            rs_facebook = request.data.get("rs_facebook"), 
            rs_twitter = request.data.get("rs_twitter"), 
            rs_linkedin = request.data.get("rs_linkedin"), 
            rs_another = request.data.get("rs_another"),
            company_name = request.data.get("company_name"),
            representative = request.data.get("representative"),
            heading = request.data.get("heading"),
            email_company = request.data.get("email_company"),
            photo = request.data.get("photo"),
            user = request.user,
            countries = country,
            cities = city,
            institution_type = request.data.get("institution_type")           
        )
        return res.id
