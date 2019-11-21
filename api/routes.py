from flask import Blueprint, jsonify
from infrastructure.repository.user import get_all
from api.serializers.user import User

bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def health():
    return jsonify(success=True), 200


@bp.route('/users')
def get_users():
    users = get_all()
    users_json = list(map(User.map, users))
    return jsonify(users_json), 200
