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

- Web Scraping Technology

  PaperPal employs advanced web scraping technology to extract relevant data, focusing on news articles from the Online Khabar portal. This feature ensures a continuous and up-to-date stream of information for users.
  <details>
    <summary> Web Scrapper </summary>
    <img src="https://github.com/Ujj1225/PaperPal/blob/main/Client%20/src/assets/images/img1.png" width=750/>
  </details>

- Sentiment Analysis

  The application utilizes sentiment analysis to evaluate the tone and sentiment of the gathered data. This feature provides users with valuable insights into how their online mentions are perceived, helping them gauge the overall sentiment surrounding their digital presence.
  <details>
    <summary> Sentiment Analysis </summary>
    <img src="https://github.com/Ujj1225/PaperPal/blob/main/Client%20/src/assets/images/img2.png" width=750/>

  </details>

- Realtime Visualization

  Implemented a visualizer where you can see the different headings/ news. It clearly helps us visualize the positive, negative and neutral topics.
  <details>
    <summary> Visualization </summary>
    <img src="https://github.com/Ujj1225/PaperPal/blob/main/Client%20/src/assets/images/img3.png" width=750/>
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
