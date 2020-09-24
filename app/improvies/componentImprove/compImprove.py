class CompImprove:
    """manage intermediate data"""

    @staticmethod
    def save_array_data(request, serializer_data):
        """save an array objects"""
        try:
            for data in request.data:
                serializer = serializer_data(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    last_improve = serializer.save()
            return last_improve.id
        except Exception as err:
            return err
