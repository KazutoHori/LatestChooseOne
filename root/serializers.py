from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
  SUQ = serializers.BooleanField()
  active = serializers.BooleanField()
  all_votes = serializers.CharField(max_length=200, read_only=True)
  author = serializers.CharField(max_length=200, read_only=True)
  category = serializers.ListField(allow_empty=True)
  choices = serializers.ListField(allow_empty=True)
  comments = serializers.ListField(allow_empty=True)
  created_at = serializers.CharField(max_length=200, read_only=True)
  created_on = serializers.CharField(max_length=200, read_only=True)
  id = serializers.IntegerField()
  likes = serializers.IntegerField()
  slug = serializers.CharField(max_length=200, read_only=True)
  users_voted = serializers.ListField(allow_empty=True)
