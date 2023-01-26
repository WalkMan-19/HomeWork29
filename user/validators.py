from datetime import date

from rest_framework.serializers import ValidationError


class CheckUserAge:
    def __call__(self, birth_date: date):
        today = date.today()
        user_age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        if user_age < 9:
            raise ValidationError(
                'Users under the age of 9 cannot register.'
            )
