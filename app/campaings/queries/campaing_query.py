from core.campaing import Campaing


class CampaingQuery(Campaing):

    @classmethod
    def get_all_campaing(cls):
        return cls.objects.filter(delete=False)

    @classmethod
    def get_by_category(cls, category):
        return cls.objects.filter(category=category, delete=False)

    @classmethod
    def get_by_city(cls, city):
        return cls.objects.filter(city=city, delete=False)

    @classmethod
    def get_by_title(cls, title):
        return cls.objects.get(title=title, delete=False)

    @classmethod
    def get_by_flag(cls, flag):
        return cls.objects.filter(flag=flag, delete=False)

    @classmethod
    def get_by_status(cls, status):
        return cls.objects.filter(status=status, delete=False)

    @classmethod
    def get_by_status_flag(cls, status, flag):
        return cls.objects.filter(status=status, flag=flag, delete=False)

    @classmethod
    def get_by_role(cls, role):
        return cls.objects.filter(role=role, delete=False)

    @classmethod
    def get_by_created(cls, dinit, dfinal):
        return cls.objects.filter(created_at__range=[dinit, dfinal], delete=False)

    @classmethod
    def get_by_ended(cls, dinit, dfinal):
        return cls.objects.filter(ended_at__range=[dinit, dfinal], delete=False)
