from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
import os

from .serializers import QuestionSerializer, UserSerializer

# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import firebase_admin.auth as auth
import threading
callback_done = threading.Event()
if not firebase_admin._apps:
    cred = credentials.Certificate('chooseone-firebase-adminsdk-lo0zg-cf95875438.json')
    firebase_admin.initialize_app(cred) 
db = firestore.client()

class QuestionsAPI(generics.ListAPIView):
  ques = []
  questions_ref = db.collection(u'questions').order_by(u'created_at', direction=firestore.Query.DESCENDING)
  for doc in questions_ref.get():
    ques.append(doc.to_dict())
  queryset = ques
  serializer_class = QuestionSerializer

class UsersAPI(generics.ListAPIView):
  # permission_classes = (permissions.IsAuthenticated, )
  users = []
  user_ref = db.collection(u'users').stream()
  for doc in user_ref:
    users.append(doc.to_dict())
  queryset = users
  serializer_class = UserSerializer

  
# class DetailAPI(generics.RetrieveAPIView):
#   permission_classes = (permissions.IsAuthenticated, )
#   ques = []
#   questions_ref = db.collection(u'questions').document(u'is-it-preferable-to-use-react-hooks-or-class-component-in-reactjs').get()
#   queryset = questions_ref
#   serializer_class = QuestionSerializer

class Assets(View):
  def get(self, _request, filename):
    path = os.path.join(os.path.dirname(__file__), 'static', filename)

    if os.path.isfile(path):
      with open(path, 'rb') as file:
        return HttpResponse(file.read(), content_type='application/javascript')
    else:
      return HttpResponseNotFound()