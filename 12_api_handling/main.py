
import requests

def fetch_rabdom_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json() # we can use json.load() from json mudule for conversion

    if data["success"] and "data" in data:
        userdata = data["data"]
        username = userdata["login"]["username"]

        return username

    else:
        raise Exception("failed to fetch userdata")

def main():
    try:
        username = fetch_rabdom_user()
        print(username)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()



