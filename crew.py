from crewai import Crew, Process
from Agents import blog_researcher, blog_writer
from Tasks import research_task, writing_task
crew = Crew(
    agents= [blog_researcher, blog_writer],
    tasks= [research_task, writing_task],
    process=Process.sequential,
    memory= True,
    max_rpm=100,
    share_crew=True

)
results = crew.kickoff(topic= {"topic": "How to GET RICH With AI Agents in 2025"})
print(results)

