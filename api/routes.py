from flask import Blueprint, jsonify


bp = Blueprint('', __name__, url_prefix='')


@bp.route('/')
def health():
    return jsonify(success=True), 200
