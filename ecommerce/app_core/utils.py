import hashlib
import time


# Media upload path factory methods
def user_avatar_path(instance):
    return '/users/{}/avatar-{}'.format(instance.email, instance.avatar.filename)


def generate_unique_id(salt):
    input_string = 'sellery' + "%.20f" % time.time() + salt
    generated_id = hashlib.sha256(input_string.encode()).hexdigest()
    return generated_id
