import streamlit as st
import pandas as pd
from datetime import datetime
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

st.set_page_config(page_title="Community Forum", page_icon="👥")
st.title("👥 Community Forum & Expert Consultation")

# Initialize session state for posts and success stories
if 'forum_posts' not in st.session_state:
    st.session_state.forum_posts = []
if 'success_stories' not in st.session_state:
    st.session_state.success_stories = []

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["Forum", "Expert Consultation", "Success Stories"])

with tab1:
    st.header("Farmer's Forum")
    st.markdown("""
    Share your experiences, ask questions, and connect with other farmers.
    """)
    
    # Create new post
    st.subheader("Create New Post")
    post_title = st.text_input("Post Title")
    post_content = st.text_area("Post Content")
    post_category = st.selectbox("Category", ["General Discussion", "Crop Issues", "Market Prices", "Equipment", "Weather", "Best Practices"])
    
    if st.button("Submit Post"):
        if post_title and post_content:
            new_post = {
                "title": post_title,
                "content": post_content,
                "category": post_category,
                "timestamp": datetime.now(),
                "author": "User",  # Could be enhanced with user authentication
                "replies": []
            }
            st.session_state.forum_posts.insert(0, new_post)
            st.success("Post created successfully!")
        else:
            st.error("Please fill in both title and content")
    
    # Display existing posts
    st.subheader("Recent Posts")
    for idx, post in enumerate(st.session_state.forum_posts):
        with st.expander(f"{post['title']} - {post['category']}"):
            st.write(f"Posted by {post['author']} on {post['timestamp'].strftime('%B %d, %Y %H:%M')}")
            st.write(post['content'])
            
            # Reply section
            reply = st.text_area("Write a reply", key=f"reply_{idx}")
            if st.button("Submit Reply", key=f"reply_button_{idx}"):
                post['replies'].append({
                    "content": reply,
                    "timestamp": datetime.now(),
                    "author": "User"
                })
                st.success("Reply posted!")
            
            # Display replies
            if post['replies']:
                st.write("Replies:")
                for reply in post['replies']:
                    st.text(f"{reply['author']} ({reply['timestamp'].strftime('%B %d, %Y %H:%M')}): {reply['content']}")

with tab2:
    st.header("Expert Consultation")
    st.markdown("""
    Get expert advice on your farming queries. Our AI expert will provide detailed responses based on agricultural best practices.
    """)
    
    # Expert consultation form
    query_type = st.selectbox("Query Type", [
        "Crop Disease",
        "Soil Management",
        "Pest Control",
        "Irrigation",
        "Market Strategy",
        "Technology Adoption",
        "Organic Farming",
        "Climate Adaptation"
    ])
    
    user_query = st.text_area("Describe your query in detail")
    
    if st.button("Get Expert Advice"):
        if user_query:
            with st.spinner("Consulting our agricultural expert..."):
                try:
                    response = client.chat.completions.create(
                        model="gpt-4-turbo-preview",
                        messages=[
                            {"role": "system", "content": "You are an expert agricultural consultant with deep knowledge of farming practices, crop management, and sustainable agriculture. Provide detailed, practical advice based on scientific principles and real-world experience."},
                            {"role": "user", "content": f"Query Type: {query_type}\n\nQuery: {user_query}\n\nPlease provide detailed advice including:\n1. Analysis of the issue\n2. Recommended solutions\n3. Preventive measures\n4. Additional resources or considerations"}
                        ]
                    )
                    st.markdown("### Expert Response")
                    st.markdown(response.choices[0].message.content)
                except Exception as e:
                    st.error(f"Error getting expert advice: {str(e)}")
        else:
            st.warning("Please enter your query")

with tab3:
    st.header("Success Stories")
    st.markdown("""
    Share your farming success stories to inspire and help other farmers learn from your experience.
    """)
    
    # Add success story
    st.subheader("Share Your Success Story")
    story_title = st.text_input("Story Title")
    crop_type = st.text_input("Crop Type")
    challenges = st.text_area("Challenges Faced")
    solutions = st.text_area("Solutions Implemented")
    outcomes = st.text_area("Outcomes and Results")
    
    if st.button("Submit Success Story"):
        if story_title and crop_type and challenges and solutions and outcomes:
            new_story = {
                "title": story_title,
                "crop_type": crop_type,
                "challenges": challenges,
                "solutions": solutions,
                "outcomes": outcomes,
                "timestamp": datetime.now(),
                "author": "User"  # Could be enhanced with user authentication
            }
            st.session_state.success_stories.insert(0, new_story)
            st.success("Success story shared!")
        else:
            st.error("Please fill in all fields")
    
    # Display success stories
    st.subheader("Featured Success Stories")
    for story in st.session_state.success_stories:
        with st.expander(f"{story['title']} - {story['crop_type']}"):
            st.write(f"Shared by {story['author']} on {story['timestamp'].strftime('%B %d, %Y')}")
            st.markdown("### Challenges")
            st.write(story['challenges'])
            st.markdown("### Solutions")
            st.write(story['solutions'])
            st.markdown("### Outcomes")
            st.write(story['outcomes']) 