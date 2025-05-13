from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson import ObjectId

chat_bp = Blueprint("protected", __name__, url_prefix="/chat")

@chat_bp.route("/perguntar", methods=["POST"])
@jwt_required()
def pergunta():
    data = request.get_json()
    pergunta = data.get("pergunta")
    auth_id = get_jwt_identity()
    # Convert string back to ObjectId if needed
    object_id = ObjectId(user_id)
    # Use object_id in DB queries
    # precisa fazer o negocio da pergunta agora
    return jsonify({"user_id": str(object_id)})
