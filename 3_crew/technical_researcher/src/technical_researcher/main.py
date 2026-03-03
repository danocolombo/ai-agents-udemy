#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from technical_researcher.crew import TechnicalCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def run():
    """
    Run the research crew.
    """
    inputs = {
        'topic': 'open brain',
        'summary': 'an open source project to retain ai prompts and data in a postgres database that can be used as a knowledge base for ai agents. The project stores vectorized data in a postgres database and uses a python api to query the database. This improves agents research because all the information and history in one agent is not in a silo from another agent. This can be used in cursor, vscode, and other ai agents that can use the api to query the database. There seems to be a project guide but seems only available for subscribers, but there may be free open source lists available.',
        'contacts': 'nate b. jones',
        'research_url': 'https://github.com/natebjj/open_brain',
        'related_projects': 'https://github.com/natebjj/open_brain_agent',
        'video_url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    }

    # Create and run the crew
    result = TechnicalCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()