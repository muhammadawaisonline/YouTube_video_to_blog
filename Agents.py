from crewai import Agent, LLM
from Tools import yt_tool

import os 
from dotenv import load_dotenv

load_dotenv()

# llm = os.getenv("OPENAI_API_KEY")

llm= LLM(
    model="gemini-1.5-flash",
    # api_key= os.getenv("GOOGLE_API_KEY")
    api_key="AIzaSyB3mgGHCUZafLtBA2FGcYfOi2DJtrStKfs"
)
## Create a Senior Blog Content Researcher

blog_researcher = Agent(
    role = "Blog Researcher From YouTube videos",
    goal = "get the relevant video links from youtube based on the topic {topic}",
    backstory= "Expert in Understanding videos in AI, Mobile Apps, Website building, Data Science , Machine Learning , AI Agents and Gen AI and providing Suggestion",
    verbose= True,
    allow_delegation= True,
    tools = [yt_tool]
)

blog_writer =  Agent(
    role= "Blog Writer",
    goal= "Narrate the compelling tech stories about the {topic}",
    backstory= "Expert in writing compelling tech stories about the {topic}",
    verbose= True,
    allow_delegation= False,
    tools = [yt_tool] 
    llm=llm
)