from crewai import Task
from Tools import yt_tool
from Agents import blog_researcher, blog_writer

## Research Task
research_task = Task(
    description=("identify the video{topic}"
    "get detailed information about the video from the channel"),
    expected_output= "A comprehensive 3 paragraph log report based on the {topic} of the video",
    tools= [yt_tool],
    agent= blog_researcher
)

## Writing Task
writing_task = Task(
    description= "write a blog post based on the {topic} of the video",
    expected_output= "A 4 paragraph blog post based on the {topic} of the video",
    tools= [yt_tool],
    agent= blog_writer
    async_execution= False,
    output_file= "blog-post.md"
)