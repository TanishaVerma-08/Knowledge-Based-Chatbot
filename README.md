# 🤖 Knowledge-Based Chatbot

This project is an Artificial Intelligence-based chatbot that operates on pre-existing knowledge provided to the system. It utilizes predefined commands to interpret user inputs and respond accordingly. A JSON file is used to store potential user questions and their respective answers.

## 📋 Project Overview

The primary objectives of this project are:

- To develop a chatbot that responds based on predefined knowledge.
- To utilize a JSON file for storing and retrieving question-answer pairs.
- To implement the chatbot using Python.

## 🛠️ Features

- **Predefined Responses**: The chatbot provides answers based on a set of predefined question-answer pairs.
- **JSON-based Knowledge Base**: Utilizes a JSON file (`Knowledge.json`) to store and manage the chatbot's knowledge base.
- **Python Implementation**: The chatbot is implemented in Python, making it easy to understand and extend.

## 🗂️ Project Structure

```
Knowledge-Based-Chatbot/
├── Knowledge.json                   # JSON file containing question-answer pairs
├── knowledge_based_chatbot.py       # Python script implementing the chatbot
└── README.md                        # Project documentation
```

## 🔧 Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/TanishaVerma-08/Knowledge-Based-Chatbot.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd Knowledge-Based-Chatbot
   ```

3. **Install the required packages**:

   Ensure you have Python installed. This project does not require any external libraries beyond the Python standard library.

## 🚀 Usage

1. **Run the Chatbot**:

   Execute the Python script to start the chatbot:

   ```bash
   python knowledge_based_chatbot.py
   ```

2. **Interact with the Chatbot**:

   Enter your questions when prompted. The chatbot will respond based on the predefined knowledge in the `Knowledge.json` file.

## 📝 Knowledge Base

The `Knowledge.json` file contains the set of predefined questions and answers that the chatbot uses to generate responses. You can modify this file to add or update the chatbot's knowledge.

## ⚠️ Note

Ensure that the `Knowledge.json` file is correctly formatted and contains the necessary question-answer pairs for the chatbot to function effectively.

