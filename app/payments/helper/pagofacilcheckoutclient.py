import hashlib


class Checkout:
    def __init__(self, string_signed):
        self.string_signed = string_signed

    def hashing_string(self):
        """begin hashing string code
        @param string
        """
        var_firma = self.string_signed.encode()
        return hashlib.sha256(var_firma).hexdigest()

    def sercret_var(self):
        commerce_id = "349c41201b62db851192665c504b350ff98c6b45fb62a8a2161f78b6534d8de9"
        token_1 = "51247fae280c20410824977b0781453df59fad5b23bf2a0d14e884482"
        token_2 = "f91e09078dbe5966e0b970ba696ec4caf9aa5661802935f86717c481f"
        token_3 = "1670e63f35d504cbddd43b7808596c935da5521eb6dc07c1d8edc1505"
        token_4 = "bf2846c2dafbf9bdc0fcf029e6133506d8dcd201f06a86dcfdc6820d8"
        token_5 = "b8683df5c03a542ac72729f1a520"
        token_service = token_1 + token_2 + token_3 + token_4 + token_5
        token_secret = "477CE8B9A98D45EDB6E5B769"
        data = {
            "token_service": token_service,
            "token_secret": token_secret,
            "commerce_id": commerce_id,
        }
        return data
