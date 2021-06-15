# --- hussein kaplan --- حسين قبلان
# استدعاء المكتبات المطلوبة
import itertools
from instagrapi import Client
import json
import os
import sys


print(sys.argv[1])
username = sys.argv[1]

def read_file(path_file, object_hook=None):

    with open(path_file, 'r', encoding='utf8') as json_file:
        return json.load(json_file, object_hook=object_hook)


if __name__ == '__main__':
    IG_CREDENTIAL_PATH = "credential.json"
    import os
    cl = None
    if os.path.exists(IG_CREDENTIAL_PATH):
        cl = Client(read_file(IG_CREDENTIAL_PATH))

user_id = cl.user_id_from_username(username)
followers = cl.user_following(user_id)
for item in followers:
    print(item)
    print("--------------------------------")
    chickstory = cl.user_stories(item)
    if chickstory != []:
        stories = cl.user_stories_gql(item)
        for itemttt in stories:
            ab = itertools.chain([itemttt.pk])
            cl.story_seen(list(ab))
