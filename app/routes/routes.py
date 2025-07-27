# from flask import Blueprint, request, jsonify
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
# from app import db
# from app.models.investment import User

# auth_bp = Blueprint('auth', __name__)

# @auth_bp.route('/register', methods=['POST'])
# def register():
#     data = request.get_json()
    
#     if User.query.filter_by(email=data['email']).first():
#         return jsonify({'message': 'Email already exists'}), 400
    
#     user = User(
#         username=data['username'],
#         email=data['email']
#     )
#     user.set_password(data['password'])
    
#     db.session.add(user)
#     db.session.commit()
    
#     return jsonify({'message': 'User created successfully'}), 201

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     user = User.query.filter_by(email=data['email']).first()
    
#     if user and user.check_password(data['password']):
#         access_token = create_access_token(identity=user.id)
#         return jsonify({
#             'access_token': access_token,
#             'user': user.to_dict()
#         }), 200
    
#     return jsonify({'message': 'Invalid credentials'}), 401