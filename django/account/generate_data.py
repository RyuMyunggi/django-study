from account.models import User


def generate_user_data(apps, schema_editor):
    """
    migrate 할 떄 user 생성
    """
    User.objects.create_superuser(
        username='admin',
        password='admin',
        name='admin',
        email='',
        gender=User.GenderChoices.MALE
    )

    for i in range(1, 10):
        username = f'user{i}'
        password = f'user{i}'
        name = f'이름{i}'
        email = f'test_email{i}@test.com'
        gender = User.GenderChoices.MALE if i % 2 == 0 else User.GenderChoices.FEMALE

        User.objects.create_user(
            username=username,
            password=password,
            name=name,
            email=email,
            gender=gender
        )
