class CompReward:
    """manage intermediate data"""

    @staticmethod
    def save_array_data(request, serializer_data):
        """save an array objects"""
        try:
            for data in request.data:
                datas = data.copy()
                datas["user"] = request.user
                serializer = serializer_data(data=datas)
                if serializer.is_valid(raise_exception=True):
                    last_reward = serializer.save()
            return last_reward.id
        except Exception as err:
            return err
