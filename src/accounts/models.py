from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()

User.add_to_class(
    "cell_phone",
    models.CharField(
        max_length=(11),
        validators=[
            MinLengthValidator(11),
        ],
        null=True,
        blank=True,
    ),
)
User.add_to_class(
    "national_code",
    models.CharField(
        max_length=(10), validators=[MinLengthValidator(10)], null=True, blank=True
    ),
)
