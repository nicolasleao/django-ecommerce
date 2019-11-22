# Media upload path factory methods
def user_avatar_path(instance):
    return '/users/{}/avatar-{}'.format(instance.email, instance.avatar.filename)