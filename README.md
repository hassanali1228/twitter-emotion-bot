<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a ![LOGO](logo.jpg)>
       <img src="images/logo.jpg" alt="Logo" width="110" height="80">
  </a>

  <h3 align="center">@wahwahbot</h3>

  <p align="center">
    A twitter bot to analyze user setiment.
    <br />
    <br />
    <a href="https://twitter.com/wahwahbot">View Profile </a>
    |

  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

The project started out with the goal of finding setiment around business announcements, in replies to their social media posts. However, the possibilities were endless when the ml model was created. After creating it, I realized it was fun for trolling around. Thus, application was containerized and hosted live, listening for twitter mentions 24/7. The bot analyzes the tweet under which it was called (@wahwahbot analyze), and returns the sentiment from the ML pipeline.


<!-- GETTING STARTED -->
## Getting Started

Download the project files and experiment with the jupyter notebook, to enhance the model. You are welcome to make a dashboard utilizing api endpoints. 

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/harshgandhi29/twitter-emotion-bot.git
   ```

2. Apply twitter api keys, and store them in an environmental file (.env)
    ```sh
    https://developer.twitter.com/en/docs/twitter-api
    consumerKey=******
    consumerSecret=******
    accessToken=******
    accessSecret=******
    ```

3. Run Docker commands.
   ```sh
   docker build . -t twitter-emotion-bot
   docker run -it twitter-emotion-bot
   ```
   
4. Troubleshoot 😉
