from smolagents import tool

@tool
def generate_tweet(topic:str)-> str: 
    """
    A tool that fetches the latest news on a topic by searching and summarizing a web page into a tweet.
    
    Args:
        topic: The topic to search for news about.
    Returns:
        str: A tweet summarizing the latest news on the topic.
    """
    return f"What is the latest news on {topic}? Please summarize it in a tweet with source."
