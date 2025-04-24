
import tweepy
from config import (
    TWITTER_API_KEY,
    TWITTER_SECRET,
    BEARER_TOKEN,
    ACCESS_TOKEN,
    ACCESS_SECRET,
)

### --------- TWITTER POST FUNCTION --------


def post_to_twitter(text):
    try:
        # Using OAuth 1.0a for user-context, still compatible with Tweepy v2 client
        client = tweepy.Client(
            consumer_key=TWITTER_API_KEY,
            consumer_secret=TWITTER_SECRET,
            access_token=ACCESS_TOKEN,
            access_token_secret=ACCESS_SECRET
        )

        response = client.create_tweet(text=text)
        print("✅ Tweet posted! Tweet ID:", response.data["id"])
    except Exception as e:
        print("❌ Twitter post failed:", e)





# ### --------- LINKEDIN POST FUNCTION ---------
# # def post_to_linkedin(text):
#     try:
#         url = "https://api.linkedin.com/v2/ugcPosts"
#         headers = {
#             "Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}",
#             "Content-Type": "application/json",
#             "X-Restli-Protocol-Version": "2.0.0"
#         }

#         payload = {
#             "author": f"urn:li:organization:{LINKEDIN_USER_URN}",
#             "lifecycleState": "PUBLISHED",
#             "specificContent": {
#                 "com.linkedin.ugc.ShareContent": {
#                     "shareCommentary": {"text": text},
#                     "shareMediaCategory": "NONE"
#                 }
#             },
#             "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
#         }

#         response = requests.post(url, headers=headers, json=payload)
#         if response.status_code == 201:
#             print("✅ Posted to LinkedIn!")
#         else:
#             print("❌ LinkedIn post failed:", response.text)
#     except Exception as e:
#         print("❌ LinkedIn post error:", e)


# ### --------- INSTAGRAM (INFO / Placeholder) ---------
# def post_to_instagram(text):
#     print("ℹ️ Instagram posting requires Meta Graph API or Instagrapi (not covered here).")
#     print("Caption would be:")
#     print(text)
