import requests


class UserInfoGetter:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_vk_info(self):
        url = f"https://api.vk.com/method/users.get?v=5.131&access_token={self.access_token}&fields=first_name,last_name,photo_200_orig"
        response = requests.get(url)
        data = response.json()['response'][0]
        pers_id = data['id']
        first_name = data['first_name']
        last_name = data['last_name']
        photo_url = data.get('photo_200_orig')
        return pers_id, first_name, last_name, photo_url

    def get_google_info(self):
        url = f"https://www.googleapis.com/oauth2/v3/userinfo?access_token={self.access_token}"
        response = requests.get(url)
        data = response.json()
        pers_id = data['sub']
        first_name = data['given_name']
        last_name = data['family_name']
        photo_url = data['picture']
        return pers_id, first_name, last_name, photo_url
