import requests


class UserInfoGetter:
    def __init__(self, access_token):
        self.access_token = access_token

    def get_vk_info(self):
        try:
            url = f"https://api.vk.com/method/users.get?v=5.131&access_token={self.access_token}&" \
                  f"fields=first_name,last_name,photo_200_orig"
            response = requests.get(url)
            data = response.json()

            if 'response' in data and len(data['response']) > 0:
                user_data = data['response'][0]
                pers_id = user_data.get('id')
                first_name = user_data.get('first_name')
                last_name = user_data.get('last_name')
                photo_url = user_data.get('photo_200_orig')
                return pers_id, first_name, last_name, photo_url
            else:
                return None, None, None, None

        except KeyError:
            return None, None, None, None

    def get_google_info(self):
        try:
            url = f"https://www.googleapis.com/oauth2/v3/userinfo?access_token={self.access_token}"
            response = requests.get(url)
            data = response.json()
            pers_id = data.get('sub')
            first_name = data.get('given_name')
            last_name = data.get('family_name')
            photo_url = data.get('picture')
            return pers_id, first_name, last_name, photo_url

        except KeyError:
            return None, None, None, None
