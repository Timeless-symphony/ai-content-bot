def generate_twitter_post(summary, url):
    # Remove https:// and replace . with [dot] to prevent link detection
    url = url.replace("https://", "").replace(".", "[dot]")
    return f"{summary}\n\n #AI #MachineLearning"#🔗 {url}


def generate_linkedin_post(summary, url):
    return f"📢 AI Update:\n{summary}\n\nRead more: {url} #ArtificialIntelligence #FutureOfWork"

def generate_instagram_post(summary, url):
    return f"🚀 New in AI!\n\n{summary}\n\nCheck out the full article here: {url}\n#AI #MachineLearning #TechTrends #Innovation"



def save_post_to_file(post_text, filename="latest_post.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(post_text)
        print(f" Post saved to {filename}")
    except Exception as e:
        print("Failed to save post to file:", e)

