from flask import Blueprint, jsonify

from app.models.user import LoginUser, RegisterUser
from app.services.auth_service import AuthService
from app.utilities.validators import validate_json

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

auth_service = AuthService()


@auth_bp.route("/register", methods=["POST"])
@validate_json(RegisterUser)
def register(user_data: RegisterUser):
    user, error = auth_service.register_user(
        name=user_data.name,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
        phone_number=user_data.phone_number,
    )
    if error:
        return jsonify({"msg": error}), 409
    return (
        jsonify(
            {
                "msg": "User created",
                "user": user.model_dump(exclude={"password_hash"}),
            }
        ),
        201,
    )


@auth_bp.route("/login", methods=["POST"])
@validate_json(LoginUser)
def login(user_data: LoginUser):
    result, error = auth_service.authenticate_user(
        email=user_data.email, password=user_data.password
    )
    if error:
        return jsonify({"msg": error}), 401
    return jsonify(result), 200
