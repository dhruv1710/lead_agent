from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from .tools.serper_tool import serper_tool
from .tools.hunter_io_tool import hunter_email_lookup
from dotenv import load_dotenv
from .models.outputs import Companies, Contacts, Emails
load_dotenv()
# Uncomment the following line to use an example of a custom tool
# from lead_agent.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool



@CrewBase
class LeadAgentCrew():
    """LeadAgent crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def business_leads_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['business_leads_researcher'],
            verbose=True,
            tools=[serper_tool],
            allow_delegation=False
        )

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            verbose=True,
            tools=[hunter_email_lookup],    
            allow_delegation=False
        )

    @agent
    def mail_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['mail_writer'],
            verbose=True,
            tools=[serper_tool],
            allow_delegation=False
        )

    @task
    def research_companies(self) -> Task:
        return Task(
            config=self.tasks_config['research_companies'],
            agent=self.business_leads_researcher(),
            output_json=Companies
        )

    @task
    def find_contacts(self) -> Task:
        return Task(
            config=self.tasks_config['find_contacts'],
            agent=self.company_researcher(),
            context=[self.research_companies()],
            output_json=Contacts
        )

    @task
    def write_emails(self) -> Task:
        return Task(
            config=self.tasks_config['write_emails'],
            agent=self.mail_writer(),
            context=[self.find_contacts()],
            output_json=Emails

        )

    @crew
    def crew(self) -> Crew:
        """Creates the LeadAgent crew"""
        return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
    
