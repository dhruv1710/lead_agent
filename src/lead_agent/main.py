#!/usr/bin/env python
import sys
from lead_agent.crew import LeadAgentCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    # niche = input("Enter the niche: ")
    # size = input("Enter the company size (small, mid, large): ")
    
    # service = input("Enter the service: ")
    size = "mid"
    niche = "automative"
    service = "AI Agents and Apps"
    inputs = {
        'topic': size,
        'niche': niche,
        'service': service
    }
    LeadAgentCrew().crew().kickoff(inputs=inputs)
    
def train():
    """
    Train the crew for a given number of iterations.
    """
    try:
        LeadAgentCrew().crew().train(n_iterations=int(sys.argv[1]))

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
