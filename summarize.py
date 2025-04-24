
import json
import requests



def summarize_article(content):
    prompt = f"Summarize the following article in 2 short sentences:\n\n{content}"

    response = requests.post(
        "http://localhost:11434/api/generate", 
        json={
            "model": "llama3.1:latest",  # Adjust model name if needed
            "prompt": prompt,
            "stream": False
        }
    )

    response.raise_for_status()
    summary = response.json()['response'].strip()  # Changed key: 'response' instead of 'message'
    return summary


# Function to summarize a list of articles and save to a JSON file
def summarize_and_save(news_list):
    summarized_data = []

    for article in news_list:
        try:
            summary = summarize_article(article["content"])
        except Exception as e:
            summary = "Error summarizing article."
            print(f"Failed to summarize: {article['title']}\nError: {e}")

        summarized_data.append({
            "title": article["title"],
            "url": article["url"],
            "summary": summary
        })
       
    # Save all summaries into a JSON file
    with open("summarized_news.json", "w", encoding="utf-8") as f:
        json.dump(summarized_data, f, indent=2, ensure_ascii=False)

    print("Summarized news saved to summarized_news.json")
     # 🔸 Print summaries in console too
    for item in summarized_data:
        print(f"📰 {item['title']}")
        print(f"📄 Summary: {item['summary']}")
        print(f"🔗 Link: {item['url']}\n")

    return summarized_data
