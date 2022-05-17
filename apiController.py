import requests
import pandas as pd
import time


class ConnectionController:
    def __init__(self):
        self.genres = []

    def getGenres(self):
        r = requests.get("https://api.jikan.moe/v4/genres/anime")
        response = r.json()
        for i in range(len(response["data"])):
            self.genres.append(response["data"][i]["name"])
        return self.genres

    def connection(self):
        url = "https://hummingbirdv1.p.rapidapi.com/anime/steins-gate"

        headers = {
            "X-RapidAPI-Host": "hummingbirdv1.p.rapidapi.com",
            "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
        }


        response = requests.request("GET", url, headers=headers)

        print(response.text)
# r = requests.get('https://hummingbirdv1.p.rapidapi.com/anime/steins-gate')
# response = r.json()
# print(response)
# data = response["data"]["title"]
# print(data)

# print(response)
# data = response["data"]["title"]
# print(data)

# for i in range(1,3):
#     r = requests.get('https://api.jikan.moe/v4/anime/' + str(i))
#     if r.status_code == 404:
#         print("code error id: " + str(i))
#         continue
#     response = r.json()
#     data = response["data"]["title"]
#     print(data)
#     time.sleep(0.5)


def dataFrame(self):
    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
    print(df)


a = ConnectionController()
# print(a.getGenres())
a.connection()
# a.dataFrame()
