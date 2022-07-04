from core.campaing import Campaing
from core.category import Category


class CategoryQuery:
    """category query"""

    @staticmethod
    def get_list_camp_header(category_slug):
        categoria = Category.objects.get(slug=category_slug)
        current_header = Campaing.objects.filter(category=categoria)
        return current_header
