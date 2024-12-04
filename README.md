# 🧟‍♂️ Hackocalypse: The LLM Survival Guide
#### *Presented by MLSA KIIT - Where AI Meets the Apocalypse*

![MLSA KIIT Banner](https://imgur.com/a/JzceXJ3)

> "In a world overrun by the undead, your AI might be humanity's last hope..."

## Table of Contents
[Overview](#overview)
[Challenge Description](#challenge-description)
[Technical Requirements](#technical-requirements)
[Getting Started](#getting-started)
[Project Structure](#project-structure)
[Implementation Guide](#implementation-guide)
[Evaluation Criteria](#evaluation-criteria)
[Submission Guidelines](#submission-guidelines)
[Resources](#resources)
[FAQ](#faq)

## Overview

Welcome to Hackocalypse, where your AI engineering skills could be the difference between survival and becoming zombie food! This hackathon challenges you to build a Retrieval-Augmented Generation (RAG) system that helps survivors navigate through an apocalyptic scenario in real-time.

Your mission is to create an LLM-powered survival assistant that processes complex map descriptions, tracks real-time updates about threats and resources, generates actionable survival plans, and adapts strategies based on changing conditions. This unique challenge combines real-time decision making with resource management, threat assessment, and geographic navigation, all powered by advanced AI technology.

## Challenge Description

### The Scenario
Imagine a city in crisis, affected by a mysterious outbreak. Your AI system serves as a lifeline for survivors, receiving and processing critical information to ensure their survival. The system works with two primary types of information:

First, you'll receive a detailed text description of the city layout, including comprehensive information about streets, highways, buildings, potential shelters, resource locations, and evacuation routes. This serves as your base map and fundamental knowledge source.

Second, your system must process continuous real-time updates covering zombie movements, weather hazards, resource availability, safe zones, and information about other survivors. This dynamic information stream requires sophisticated processing and integration with your base knowledge.

### Your Task
Your challenge is to build a RAG-based system using the Groq API that expertly handles this complex information landscape. The system should maintain constant awareness of the map layout while processing and remembering real-time updates. Most importantly, it must generate clear, actionable survival plans that consider all available information.

## Technical Requirements

Your development environment should include Python 3.7 or higher and Git. During the hackathon, you'll receive access to the Groq API, which will serve as your primary LLM interface. The core project dependencies include:

```plaintext
groq             # For LLM integration
faiss-cpu        # Vector storage and search
streamlit        # Web interface
python-dotenv    # Environment management
requests         # API handling
numpy            # Numerical operations
```

For optimal development experience, we recommend using a virtual environment tool (venv or conda), an IDE such as VS Code or PyCharm, and Postman for API testing.

## Getting Started

Setting up your development environment is straightforward. Here's how to get started:

```bash
# Clone the template repository
git clone https://github.com/MLSA-KIIT/hackocalypse-template.git
cd hackocalypse-template

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

Our template provides a carefully organized project structure to help you get started quickly:

```plaintext
hackocalypse/
├── docs/                           # Documentation
│   ├── problem_statement.md        # Detailed problem description
│   ├── evaluation_criteria.md      # Scoring guidelines
│   ├── technical_setup.md         # Setup instructions
│   └── scenarios/                 # Sample scenarios
│       └── sample_scenario_1/
│           ├── map_description.txt # Base map information
│           └── updates.json        # Sample real-time updates
├── src/
│   ├── baseline/                  # Basic implementation
│   │   ├── retriever.py          # Data retrieval system
│   │   └── generator.py          # Response generation
│   └── utils/
│       ├── groq_client.py        # Groq API wrapper
│       └── data_loader.py        # Data handling utilities
├── tests/                        # Test files
│   └── test_baseline.py         # Basic tests
├── README.md                     # This file
├── requirements.txt              # Project dependencies
└── .gitignore                   # Git ignore rules
```

## Implementation Guide

The key to success lies in understanding and effectively implementing two core components: the Retriever and the Generator.

The Retriever, implemented in `src/baseline/retriever.py`, serves as your information management system. It processes and indexes the map description, manages real-time updates, and implements vector search for relevant information. Here's a basic example of its structure:

```python
class Retriever:
    def __init__(self):
        self.map_index = None
        self.updates = []
    
    def index_map(self, map_description: str):
        # Process and index map description
        pass
    
    def add_update(self, update: dict):
        # Process and store new updates
        pass
    
    def get_relevant_context(self, query: str):
        # Retrieve relevant information
        pass
```

The Generator, found in `src/baseline/generator.py`, handles all interactions with the Groq API. It formats prompts with retrieved context and generates responses. Here's its basic structure:

```python
class Generator:
    def __init__(self, groq_client):
        self.client = groq_client
    
    def generate_response(self, query: str, context: str):
        # Generate response using Groq
        pass
```

Your implementation should focus on three key areas: First, develop robust map processing capabilities that efficiently parse and index descriptions while maintaining spatial relationships. Second, create sophisticated update management that processes real-time information and maintains temporal context. Finally, implement response generation with effective prompting strategies and actionable outputs.

## Evaluation Criteria

Your solution will be evaluated based on two main categories: Technical Assessment (60%) and Scenario Success (40%). The technical assessment examines your system's accuracy in information retrieval, quality of generated responses, system response time, and context maintenance. Scenario success evaluates the effectiveness of survival strategies, resource management, threat avoidance, and route planning.

## Submission Guidelines

To submit your solution, fork the template repository and implement your solution. Create comprehensive documentation of your approach, including system architecture overview, implementation decisions, setup instructions, and sample interactions. Submit your final work via PR to the main repository.

## Resources

We've compiled extensive documentation to support your development journey. You'll find the official documentation for all core technologies:

The Groq API documentation (https://docs.groq.com) provides detailed information about LLM integration.
FAISS documentation (https://github.com/facebookresearch/faiss/wiki) covers vector search implementation.
Streamlit documentation (https://docs.streamlit.io) helps with building your interface.

Additionally, we recommend reviewing guides on RAG systems, vector search tutorials, and prompt engineering best practices.

## FAQ

We've compiled answers to common questions participants might have:

The use of additional APIs is permitted, but core functionality must utilize Groq. System stability is crucial and factors into evaluation, with crashes potentially impacting your score. While you can modify the project structure, maintaining clear organization and documentation is essential. Response time limits are set at 5 seconds maximum per response to ensure practical usability.

## Support

The MLSA KIIT team is here to support you throughout the hackathon. Reach us through:

Discord: [MLSA KIIT Server](https://discord.gg/DymVbhCmJf)
Instagram: [@mlsakiit](https://instagram.com/mlsakiit)

## Code of Conduct

All participants must adhere to our Code of Conduct, which ensures a respectful and inclusive environment for everyone. Review it at [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

This project operates under the MIT License. For full details, see the [LICENSE](LICENSE) file.

---
Made with 🧟‍♂️ by MLSA KIIT

*Remember: In the apocalypse, your code might be someone's last hope. Make it count.*
