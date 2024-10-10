""" This Section handles all the endpoints that are related to the posts """
from flask import Blueprint, request, jsonify, g
from models import Post
from serializers import PostSerializer
from validations import validate_post_data
from auth import jwt_required

post_bp = Blueprint('post_bp', __name__)

@post_bp.route('/post', methods=['POST'])
@jwt_required
def create_post():
    try:
        data = request.json
        validation_error = validate_post_data(data)
        if validation_error:
            return validation_error
        
        post_serializer = PostSerializer(None)
        post = post_serializer.deserialize(data)
        post.user_id = g.user_id 
        Post.create(post)
        return jsonify(post.to_json()), 201 
    except:
        return jsonify({"error": "Can not create this post"}), 400


@post_bp.route('/post/<int:post_id>', methods=['GET'])
@jwt_required
def get_post(post_id):
    try:
        post_data = Post.get_post(post_id)
        if not post_data:
            return jsonify({"error": "This post not found"}), 404
        post_serializer = PostSerializer(post_data)
        return jsonify(post_serializer.serialize()), 200
    except:
        return jsonify({"error": "Can not find this post"}), 400


@post_bp.route('/post/<int:post_id>', methods=['PUT'])
@jwt_required
def update_post(post_id):
    try:
        data = request.json
        content = data.get('content')
        if not content:
            return jsonify({"error": "Content is required"}), 400
        post_data = Post.get_post(post_id)
        if not post_data:
            return jsonify({"error": "This post not found"}), 404
        post = Post.update(post_id, content)
        post_serializer = PostSerializer(post)
        return jsonify({"message": "Post updated successfully","data":post_serializer.serialize()}), 200
    except:
        return jsonify({"error": "Can not update this post"}), 400

# Delete Post
@post_bp.route('/post/<int:post_id>', methods=['DELETE'])
@jwt_required
def delete_post(post_id):
    try:
        post_data = Post.get_post(post_id)
        if not post_data:
            return jsonify({"error": "This post not found"}), 404
        Post.delete(post_id)
        return jsonify({"message": "Post deleted successfully"}), 200
    except:
        return jsonify({"error": "Can not delete this post"}), 400