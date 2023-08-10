# shodan-server
# shodan
# Shodan API

![Python](https://img.shields.io/badge/python-v3.8-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-v0.68.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

Shodan API is a FastAPI backend designed to integrate with vector databases, LangChain, HuggingFace, OpenAI, and frontend frameworks like Flutter. This project aims to provide a robust and scalable backend solution for AI and machine learning applications.

## Features

- FastAPI backend for high performance
- Integration with vector databases for efficient data storage and retrieval
- Utilizes LangChain for language processing
- Incorporates HuggingFace and OpenAI for advanced AI capabilities
- Designed to work with frontend frameworks like Flutter

## Installation

We use Poetry for dependency management. It handles both the package installation and the virtual environment for you.

First, ensure you have Poetry installed. If not, $bash install it globally:

`curl -sSL https://install.python-poetry.org | python - `

Then, from the project's root directory, install the project's dependencies:

`poetry install`

## To start the server

`$ uvicorn main:shodan_api --reload`

- The server will start at http://localhost:8000/.
- You can view the Swagger UI at http://localhost:8000/docs. This is were you can test the API endpoints.

## Persistent Endpoints
`https://shodan.site/`


License : [MIT](https://choosealicense.com/licenses/mit/)

"SHODAN", "TriOptimum", and "System Shock" are registered trademarks of [Night Dive Studios](https://nightdivestudios.com/).

"shodan.io" is a registered trademark of [John Matherly](https://twitter.com/achillean). This project is not affiliated with Shodan Inc. in any way.
