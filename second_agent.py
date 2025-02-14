from smolagents import CodeAgent, DuckDuckGoSearchTool, VisitWebpageTool, HfApiModel, tool
from tools.generate_tweet import generate_tweet  

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), VisitWebpageTool()], 
    model=HfApiModel()
)

agent.run(generate_tweet("AI agents")) 