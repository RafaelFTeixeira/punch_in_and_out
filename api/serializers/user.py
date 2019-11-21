import json


class User(json.JSONEncoder):
    @staticmethod
    def map(o):
        return {
            'id': o.id,
            'name': o.name,
            'email': o.email
        }
