import random
from .models import *
from .serializers import *


def get_random_message_by_category(category):
    messages = Message.objects.filter(categoria=category)
    serializer = MessageSerializer(instance=messages, many=True)

    temp_list = []
    for data in serializer.data:
        temp_list.append(data['id'])

    random_index = random.randint(0, len(temp_list)-1)
    random_id = temp_list[random_index]

    message = Message.objects.get(id=random_id)

    return message.message