import factory
from django.contrib.auth import get_user_model
User = get_user_model()

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User

    email = 'admin@admin.com'
    username = 'admin'
    password = 'adm1n'

    is_superuser = True
    is_staff = True  
    is_active = True

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop('password', None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user
