import streamlit as st
from fetch_news import fetch_ai_news
from summarize import summarize_article
from generate_post import (generate_twitter_post,
    generate_linkedin_post,
    generate_instagram_post)
from post import post_to_twitter
                  #, post_to_linkedin,post_to_instagram)

st.title("🤖 AI News to Twitter Bot")

if st.button("Fetch & Post News"):
    news_list = fetch_ai_news()
    for article in news_list:
        summary = summarize_article(article["content"])
        twitter_post = generate_twitter_post(summary, article["url"])
        #linkedin_post = generate_linkedin_post(summary, article["url"])
        #instagram_post = generate_instagram_post(summary, article["url"])
        post_to_twitter(twitter_post)
        st.success("✅ Posted to Twitter")

        # post_to_linkedin(linkedin_post)
        # st.success("✅ Posted to LinkedIn")

        # post_to_instagram(instagram_post)
        # st.success("✅ Instagram post prepared (print only unless using Instagrapi)")

    st.balloons()