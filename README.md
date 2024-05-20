# PaperPal

# <p align="center"><img src="https://github.com/Ujj1225/PaperPal/blob/main/Client%20/src/assets/images/hero-socialmedia.png" width=300 /></p>

<p align="center">
    <p align="center">
        <a href="https://github.com/Ujj1225/PaperPal" target="blank">
            <img src="https://img.shields.io/github/watchers/Ujj1225/PaperPal?style=for-the-badge&logo=appveyor" alt="Watchers"/>
        </a>
        <a href="https://github.com/Ujj1225/PaperPal/fork" target="blank">
            <img src="https://img.shields.io/github/forks/Ujj1225/PaperPal?style=for-the-badge&logo=appveyor" alt="Forks"/>
        </a>
        <a href="https://github.com/Ujj1225/PaperPal/stargazers" target="blank">
            <img src="https://img.shields.io/github/stars/Ujj1225/PaperPal?style=for-the-badge&logo=appveyor" alt="Star"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/Ujj1225/PaperPal/issues" target="blank">
            <img src="https://img.shields.io/github/issues/Ujj1225/PaperPal?style=for-the-badge&logo=appveyor" alt="Issue"/>
        </a>
        <a href="https://github.com/Ujj1225/PaperPal/pulls" target="blank">
            <img src="https://img.shields.io/github/issues-pr/Ujj1225/PaperPal?style=for-the-badge&logo=appveyor" alt="Open Pull Request"/>
        </a>
    </p>
    <p align="center">
        <a href="https://github.com/Ujj1225/PaperPal/blob/master/LICENSE" target="blank">
            <img src="https://img.shields.io/github/license/Ujj1225/PaperPal?style=for-the-badge&logo=appveyor" alt="License" />
        </a>
    </p>
</p>

<p align="center">
</p>

## Problem Statement

# <p align="center"><img src="https://github.com/Ujj1225/PaperPal/blob/main/Client%20/src/assets/images/problem.png" width=750 height=425 /></p>

## Solutions

# <p align="center"><img src="https://github.com/Ujj1225/PaperPal/blob/main/Client%20/src/assets/images/Solution.png" width=750 height=425 /></p>

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Dependencies](#dependencies)
- [License](#license)

## Features

- Research Paper Summarization

The application uses advanced natural language processing (NLP) techniques to generate concise summaries of research papers. This feature helps users quickly understand the key points and findings of lengthy academic documents.
<details>
  <summary> Paper Summarization </summary>
  <img src="https://github.com/yourusername/yourrepository/blob/main/path/to/summarization_example.png" width=750/>
</details>

- Question and Answer System

The system leverages state-of-the-art models to answer questions about the content of research papers. By providing detailed explanations alongside the answers, this feature enables users to gain a deeper understanding of specific aspects of the research.
<details>
  <summary> Question and Answer </summary>
  <img src="https://github.com/yourusername/yourrepository/blob/main/path/to/qa_example.png" width=750/>
</details>

- User-Friendly Interface

The platform includes a clean and intuitive interface where users can easily upload research papers, ask questions, and view summaries and answers. This feature ensures that even users without technical expertise can benefit from the application's capabilities.
<details>
  <summary> User Interface </summary>
  <img src="https://github.com/yourusername/yourrepository/blob/main/path/to/ui_example.png" width=750/>
</details>

## Installation

### Prerequisites

Before running PaperPal, you must set it up by following the given setup procedure. You must set up the Frontend, Backend and Model separately. In case of any query, feel free to contact the contributors.

### Setup

#### Follow the given steps to set up walletWISE

1. Clone the repository:

   ```bash
   git clone https://github.com/Ujj1225/PaperPal.git
   ```

2. Installation of required packages

### Frontend

```bash
cd client
npm install
```

### Backend

```bash
cd backend
npm install
```

### Model 
```bash
cd model
pip install llmware
```

3. Setting up .env file for Backend

- Create a .env file

  ```bash
  PORT = (You can use any but default is: 3000)
  ```

4. Running the project:

- Frontend and Backend file must be run together.

#### Frontend

- Navigate to Client then:

```bash
  npm run dev
```

#### Backend

- Navigate to Backend then:

```bash
  node app.js
```

# You are all set to use the application!

## Dependencies

### Frontend

- For frontend can be found in [package.json](./Client%20/package.json)

### Backend

- For backend can be found in [package.json](./Backend/package.json)

### Model

- LLMWare's specialized model namely "slim-summary-tool" and "slim-boolean-tool" is used for this project. 

## License

This project is licensed under the [MIT License](/LICENSE).
