from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from .serializers import QuestionSerializer

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

class QuestionsAPI(ListAPIView):
  ques = []
  questions_ref = db.collection(u'questions').order_by(u'created_at', direction=firestore.Query.DESCENDING)
  for doc in questions_ref.get():
      ques.append(doc.to_dict())
  queryset = ques
  serializer_class = QuestionSerializer

def root(request):
  return render(request, 'index.html', {})