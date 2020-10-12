from core.currency import Currency


class CurrencyQuery:
    @staticmethod
    def get_currency(name_currency):
        return Currency.objects.get(name=name_currency)
