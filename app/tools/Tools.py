from datetime import datetime


class EndDate:

    @classmethod
    def cal_days(cls, public, ended):
        """rules
        - public date may have grater than ended date
        TODO: date public remove timezone
            date ended remove timezone
        """
        date_public = datetime.strptime(str(public), '%Y-%m-%d %H:%M:%S')
        date_ended = datetime.strptime(str(ended), '%Y-%m-%d %H:%M:%S')

        if date_ended > date_public:
            end_date = date_ended - date_public
            return end_date.days
        return False
