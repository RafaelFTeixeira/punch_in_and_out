from infrastructure.mapper.user import User


def get_all():
    return User.query.all()
