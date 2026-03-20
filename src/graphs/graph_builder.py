from langgraph.graph import START, END, StateGraph
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState
from src.nodes.blognode import BlogNode

class GraphBuilder:
    def __init__(self,llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate a blog on the given topic.
        """
        # Nodes
        # define the `title_creation` and `content_generation` nodes
        blog_node = BlogNode(self.llm)
        self.graph.add_node("title_creation", blog_node.title_creation)

        self.graph.add_node("content_generation", blog_node.content_generation)

        # edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        # return the compiled graph
        return self.graph.compile()
    
    def setup_graph(self, usecase):
        if usecase == "topic":
            return self.build_topic_graph()
    