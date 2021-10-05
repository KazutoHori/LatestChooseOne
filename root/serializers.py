from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
  SUQ = serializers.BooleanField()
  active = serializers.BooleanField()
  all_votes = serializers.CharField(max_length=200, read_only=True)
  author = serializers.CharField(max_length=200, read_only=True)
  category = serializers.ListField(default = [])
  choices = serializers.ListField(default = [])
  comments = serializers.ListField(default = [])
  created_at = serializers.CharField(max_length=200, read_only=True)
  created_on = serializers.CharField(max_length=200, read_only=True)
  id = serializers.IntegerField()
  likes = serializers.IntegerField()
  slug = serializers.CharField(max_length=200, read_only=True)
  title = serializers.CharField(max_length=200, read_only=True)
  users_voted = serializers.ListField(default = [])

class UserSerializer(serializers.Serializer):
  created_at = serializers.CharField(max_length=200, read_only=True)
  email = serializers.CharField(max_length=200, read_only=True)
  question_created = serializers.ListField(default = [])
  question_liked = serializers.ListField(default = [])
  question_voted = serializers.ListField(default = [])
  uid = serializers.CharField(max_length=200, read_only=True)
  username = serializers.CharField(max_length=200, read_only=True)

