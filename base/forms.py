from django.forms import ModelForm
from .models import Room, Message, Topic

class RoomForm(ModelForm):
  class Meta:
    model = Room
    fields = '__all__'
    exclude = ['host','participants']

class MessageForm(ModelForm):
  class Meta:
    model = Message
    fields = ['body']

class TopicForm(ModelForm):
  class Meta:
    model = Topic
    fields = '__all__'