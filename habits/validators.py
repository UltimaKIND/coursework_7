from rest_framework.serializers import ValidationError


class HabitValidator:

    def __call__(self, data):
        self.validate_related_habit_or_reward(data)
        self.validate_related_habit(data)
        self.validate_is_pleasant_habit(data)
        self.validate_time_to_action(data)

    def validate_related_habit_or_reward(self, data):
        """
        Можно выбрать или вознаграждение или приятную привычку, но не вcе сразу.
        """
        if data.get("related_habit") and data.get("reward"):
            raise ValidationError(
                "Можно выбрать или вознаграждение или приятную привычку, но не все сразу"
            )

    def validate_time_to_action(self, data):
        """
        Время выполнения привычки не может быть больше 120 секунд
        """
        if data.get("time_to_action", 0) > 120:
            raise ValidationError(
                "Время выполнения привычки не может быть больше 120 секунд."
            )

    def validate_related_habit(self, data):
        """
        В связаные привычки можно выбрать только приятные.
        """
        related_habit = data.get("related_habit")
        if related_habit and not related_habit.is_pleasant:
            raise ValidationError("В связанные привычки можно выбрать только приятные.")

    def validate_is_pleasant_habit(self, data):
        """
        У приятной привычки не может быть связанной привычки или вознаграждения
        """
        if data.get("is_pleasant"):
            if data.get("reward") or data.get("related_habit"):
                raise ValidationError(
                    "У приятной привычки не может быть связанной привычки или вознаграждения"
                )
