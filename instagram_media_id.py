import requests
import json

class Find_Id:
    """
        Docstring:  if the instagram post not private.
        input: url = İnstagram Media link
        output: media_id, user_id or ex
    """
    def __init__(self,url) -> None:
        self.mediaurl=url

    def findid(self):
        try:
            html = requests.get("http://api.instagram.com/oembed?url={}".format(self.mediaurl)).content
            media_json = json.loads(html.decode('utf-8'))
            media_id=media_json["media_id"]
            user_id=media_id.split("_")[1]
            print(user_id)
            return {'media_id': media_id,"user_id":user_id ,'ex': ''}
        except Exception as ex:
            return {'ex': f'Find id hatasi : {ex}'}


