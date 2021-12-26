



# 1. import package
import tweepy

# 2. Store credentials
apiKey = "LFuvye8aE8YamnPSYNMoMfxoi"
apikeySecret = "dOoHGuUWf2PtK0RtLVEyHCNnUPMbkJHJkif1eRkWKKvoX5CA8P"

accessToken = "3068409066-aRv2vgSxuFvltPKF0LjFL035Sm9CHtwaTvhWLxQ"
accessTokenSecret = "MK5f0rEAX6AjSA6H5Rd6nRsaYWHUlwCNZjfTfkIflbcvv"


# 3. Create Oauth client and set authentication and create API object
oauth = tweepy.OAuthHandler(apiKey, apikeySecret)
oauth.set_access_token(accessToken, accessTokenSecret)
print("Authentication successfully")

api = tweepy.API(oauth)


# 4. upload media
media = api.media_upload("Twitter-limitation.png")

result = api.update_status(status = "Uploaded using Tweepy python module",media_ids = [media.media_id_string])

print("Uploaded successfully")