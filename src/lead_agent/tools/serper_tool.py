import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
load_dotenv()
os.environ['SERPER_API_KEY'] = 'd61d6e06a4e708547ead52468cd5c3d1678fb7f4'

# inititlaize the tool for internet searching capabilities
serper_tool = SerperDevTool()


