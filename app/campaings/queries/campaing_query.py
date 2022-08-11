from core.campaing import Campaing


class CampaingQuery:


    @classmethod
    def get_all(cls):
        return Campaing.objects.filter(delete=False)

    @classmethod
    def get_by_category(cls, category):
        return Campaing.objects.filter(category=category, delete=False)

    @classmethod
    def get_by_city(cls, city):
        return Campaing.objects.filter(city=city, delete=False)

    @classmethod
    def get_by_title(cls, title):
        return Campaing.objects.filter(title__contains=title, delete=False)

    @classmethod
    def get_by_exact_title(cls, title):
        return Campaing.objects.get(title=title, delete=False)

    @classmethod
    def get_by_campaing_id(cls, campaing_id):
        return Campaing.objects.get(id=campaing_id, delete=False)

    @classmethod
    def get_by_flag(cls, flag):
        return Campaing.objects.filter(flag=flag, delete=False)

    @classmethod
    def get_by_status(cls, status):
        return Campaing.objects.filter(status=status, delete=False)

    @classmethod
    def get_by_status_flag(cls, status, flag):
        return Campaing.objects.filter(status=status, flag=flag, delete=False)

    @classmethod
    def get_by_role(cls, role):
        return Campaing.objects.filter(role=role, delete=False)

    @classmethod
    def get_by_created(cls, dinit, dfinal):
        return Campaing.objects.filter(
                created_at__range=[dinit, dfinal],
                delete=False
        )

    @classmethod
    def get_by_ended(cls, dinit, dfinal):
        return Campaing.objects.filter(
                ended_at__range=[dinit, dfinal],
                delete=False
        )
