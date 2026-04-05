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
        'topic': 'Portable AI Memory',
        'summary': 'A lot of today’s AI tools and agents lack durable, portable “memory,” forcing you to re-explain your projects, constraints, decisions, and context every time you switch chats or platforms. The transcript argues that this memory gap—not model quality—is becoming the real bottleneck to effective prompting, context engineering, and agent usefulness, and that vendor-specific memory features create lock-in while remaining siloed across tools (Claude, ChatGPT, Cursor, etc.). As a solution, it proposes an “Open Brain”: a personal, database-backed knowledge system you own, built on a boring/reliable PostgreSQL store plus vector embeddings (semantic search) and exposed through MCP so any compatible AI client or agent can both write memories (capture) and read them (retrieve). With fast capture from tools like Slack and universal retrieval via MCP, the system enables consistent cross-tool context, supports compounding productivity over time, and remains future-proof and low-cost compared to proprietary SaaS memory layers.',
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