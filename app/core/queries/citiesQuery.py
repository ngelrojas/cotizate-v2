from core.city import City


class CitiesQuery:
    """city queries"""

    @staticmethod
    def get_list_cities():
        """get list all cities"""
        return City.objects.all()

    @staticmethod
    def retrieve_cities(country_id, pk):
        """retrieve cities"""
        return City.objects.get(countries=country_id, id=pk)
