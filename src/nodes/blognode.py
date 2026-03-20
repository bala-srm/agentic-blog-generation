
from src.states.blogstate import BlogState


class BlogNode:
    """
    A class whose instances represent a node in the blog generation graph. 
    Each node will have a specific function, such as generating the title or content of the 
    blog post.
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        Generate a title for the blog post based on the given topic.
        
        Args:
            state (BlogState): The current state of the blog generation process, which includes the topic.
        
        Returns:
            str: The generated title for the blog post.
        """
        # Implement the logic to generate the title using the LLM
        
        if "topic" in state and state["topic"]:
            topic = state["topic"]
            prompt = f"""
            You are an expert blog writer. Using markdown formatting, generate a catchy, relevant and 
            SEO friendly title for the blog post on the topic: "{topic}". The title should be 
            concise, engaging, and accurately reflect the content of the blog post.
            """
            system_message = prompt.format(topic=topic)
            response = self.llm.invoke(system_message)
            return {"blog":{"title": response.content}}
        
    def content_generation(self, state: BlogState):
        """
        Generate the content for the blog post based on the given title and topic.
        
        Args:
            state (BlogState): The current state of the blog generation process, which includes the topic and title.
        
        Returns:
            str: The generated content for the blog post.
        """
        # Implement the logic to generate the content using the LLM
        
        if "topic" in state and state["topic"]:
            topic = state["topic"]
            title = state["blog"]["title"]
            prompt = f"""
            You are an expert blog writer. Using markdown formatting, generate a detailed, informative, and engaging 
            blog post based on the following title and topic:
            
            Title: "{title}"
            Topic: "{topic}"
            
            The content should be well-structured with an introduction, body, and conclusion. It should provide valuable 
            insights, examples, and actionable information related to the topic. Ensure that the content is original, 
            free of plagiarism, and adheres to SEO best practices.
            """
            system_message = prompt.format(title=title, topic=topic)
            response = self.llm.invoke(system_message)
            return {"blog":{"content": response.content}}