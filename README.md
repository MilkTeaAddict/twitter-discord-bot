# Twitter Discord Bot

A Python-based Twitter Discord bot that streams live tweets based on search terms and allows users to fetch the latest tweets from specific Twitter accounts.

## Features
- Streams live tweets matching specific keywords and posts them to a Discord channel.
- Fetches and displays recent tweets from a specified Twitter account.
- Built with Tweepy and Discord API, utilizing asyncio for asynchronous communication.

## Table of Contents
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/twitter-discord-bot.git
    cd twitter-discord-bot
    ```

2. **Install dependencies:**

    Make sure you have [Python 3.8+](https://www.python.org/downloads/) installed. Then install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    You'll need to provide your Twitter API and Discord credentials. You can do this by creating an `.env` file or exporting them in your shell environment.

    **.env example:**
    ```bash
    TWITTER_API_KEY=your_api_key
    TWITTER_API_KEY_SECRET=your_api_key_secret
    TWITTER_BEARER_TOKEN=your_bearer_token
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret
    ```

4. **Configure the bot:**

    Set up your Discord bot and configure it to connect to your Discord server. Instructions can be found in the [Discord Developer Portal](https://discord.com/developers/applications).

## Setup

1. **Twitter Developer Setup:**
    - Create a [Twitter Developer account](https://developer.twitter.com/en/apps).
    - Generate your API keys, tokens, and bearer token.
    - Replace the placeholder values in `.env` with your actual credentials.

2. **Discord Bot Setup:**
    - Create a new bot in the [Discord Developer Portal](https://discord.com/developers/applications).
    - Invite the bot to your server with appropriate permissions.
    - Replace the placeholder values in `.env` with your Discord bot token.

## Usage

1. **Running the bot:**

    After setting up the environment and installing dependencies, you can start the bot by running:

    ```bash
    python bot.py
    ```

2. **Bot commands:**
    - The bot streams tweets based on keywords you define in the `search_terms` list.
    - You can use the bot to fetch tweets from a specific user by sending a command in your Discord server: `!tweets username`


