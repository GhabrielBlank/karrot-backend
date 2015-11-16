from .initial_data import request_user, chat

request = {
    "endpoint": "/api/chats/{}/messages".format(chat.id),
    "method": "post",
    "user": request_user,
    "body": {
        "content": "Hello Matthias!",
    }
}
