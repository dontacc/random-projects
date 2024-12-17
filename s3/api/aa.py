import uuid

uuid = str(uuid.uuid4().hex)
print(uuid)

b = "/".join([uuid[i:i+2] for i in range(0, 10, 2)]) + uuid[10:]
