# Hugging Face AI Agents course

## Project Description
This project demonstrates the use of the `smolagents` library to create AI agents that uses tools and Hugging Face API model.

## Installation
This project requires Python. 
To install the required dependencies, you can use the following command:
```bash
pip install smolagents
pip install smolagents[gradio]
```

## Usage
To use Smolagents, you can follow these steps:
1. Register or login on https://huggingface.co/
2. Create free token at https://huggingface.co/settings/tokens  
**Note:** *Make sure Inference - Make calls to inference providers is checked.*
3. Use the command **huggingface-cli login** and paste the token
4. Run the files with python command, for example:
```bash
python second_agent.py
```

## Agents
**first_agent.py**  
Example of how you can get an agent up and running with just 3 lines of code. This agent calculates a query by searching the web.

**second_agent.py**  
This shows how we can use a custom tool for our agent. This agent summarizes news on a topic into a tweet.

**third_agent.py**  
This shows how we can use GradioUI to launch an interactive user interface. This agent uses a text-to-image image generation tool.