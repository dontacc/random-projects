def generate_room_name(sender_id, receiver_id):
    if sender_id > receiver_id:
        return f"chat-{sender_id}-{receiver_id}"
    return f"chat-{receiver_id}-{sender_id}"
