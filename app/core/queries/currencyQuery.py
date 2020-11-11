from core.currency import Currency


class CurrencyQuery:
    @staticmethod
    def get_currency(currency_id):
        return Currency.objects.get(id=currency_id)
