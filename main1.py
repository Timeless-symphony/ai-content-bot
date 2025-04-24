from fetch_news import fetch_ai_news
from summarize import summarize_article, summarize_and_save
from generate_post import generate_twitter_post, save_post_to_file
from post import post_to_twitter

def main():
    # Step 1: Fetch AI news articles
    articles = fetch_ai_news()
    if not articles:
        print("❌ No AI articles found.")
        return
    print("✅ Fetched news saved to fetched_news.json")

    # Take the first article with content
    article = articles[0]
    content = article.get("content", "")
    url = article.get("url", "")
    title = article.get("title", "Untitled Article")

    if not content:
        print("❌ Article has no content.")
        return

    # Step 2: Summarize and save
    summary = summarize_article(content)
    summarize_and_save([article])  # ⬅️ Automatically saves summary to file
    print("✅ Summary saved to summarized_news.json")

    # Step 3: Generate post and save
    post_text = generate_twitter_post(summary, url)
    save_post_to_file(post_text)  # ⬅️ Automatically saves post to file
    print("✅ Post saved to latest_post.txt")

    # Step 4: Post to Twitter
    post_to_twitter(post_text)

if __name__ == "__main__":
    main()

