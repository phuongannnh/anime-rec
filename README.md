# Anime Recommendation System

## Introduction
Hey there! Welcome to my data analysis project on anime recommendations. As a huge anime fan, I thought it would be super fun to combine my love for anime with my data analysis skills to create a recommendation system for other anime watchers. This project dives into user preferences and anime ratings to help everyone find fun new anime to watch.

## Objective
The main goal here is to dig into user preferences and anime ratings to make a kickass anime recommendation system. By using the datasets, I want to find trends, figure out what influences ratings, and build a system that suggests anime you'll love. I'll also use PowerBI to make some cool visualizations to show off the findings.

### Specific Objectives
1. **See how genre and ratings connect**: Find out which genres get the best ratings.
2. **Discover the top 10 most popular anime**: Based on user ratings and member count.
3. **Analyze how users rate anime**: Understand rating patterns for different types of shows.
4. **Make personalized anime suggestions**: Develop a system to recommend anime based on what users like.
5. **Showcase the findings visually**: Use PowerBI to create eye-catching visualizations.

## Datasets
The analysis is based on two main datasets, which are pulled from kaggle.com (https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database?resource=download).

- **anime.csv**: Details about various anime shows, like genre, type, episodes, ratings, and member count.
- **rating.csv**: User ratings for different anime shows, with each entry showing a user's rating for a specific anime.

## Tools and Technologies
- **Python**: For data processing and analysis in a Jupyter notebook.
- **SQL**: For running complex queries and data manipulation.
- **PowerBI**: To create cool visualizations and present the findings.

## Steps and Deliverables
1. **Ask**: Define what we want to achieve and key factors.
2. **Prepare**: Gather and clean up the data.
3. **Process**: Check data quality and get it ready for analysis.
4. **Analyze**: Dig into the data to find insights.
5. **Share**: Create visualizations and show off the findings.
6. **Act**: Highlight the main takeaways and suggest next steps.


## Objectives and Results

### 1. Understanding the Connection Between Genre and Ratings
- **Analysis**: Analyzed the distribution of ratings across different genres to identify which genres tend to receive higher ratings.
- **Results**:
  - Genres like **Action, Adventure, Drama, Fantasy, Magic, Military, and Shounen** often have higher average ratings.

### 2. Identifying the Top 10 Most Popular Anime
- **Analysis**: Ranked anime by rating to identify the top 10 most popular ones.
- **Results**:
  - Top 10 anime by rating:
    - **Taka no Tsume 8: Yoshida-kun no X-Files**
    - **Spoon-hime no Swing Kitchen**
    - **Mogura no Motoro**
    - **Kimi no Na wa**
    - **Kahei no Umi**
    - **Fullmetal Alchemist: Brotherhood**
    - **Gintama**
    - **Yakusoku: Africa Mizu to Midori**
    - **Steins;Gate**
    - **Gintama&#039**

### 3. Analyzing User Ratings of Anime
- **Analysis**: Explored the distribution of user ratings and how these ratings vary by anime type.
- **Results**:
  - Most user ratings are clustered around 6-8. This indicates that while there are extremes on either end of the rating scale, a significant proportion of users tend to give moderate ratings. This clustering suggests a balanced perspective from viewers, with fewer users rating anime as either very poor (1-3) or exceptionally high (9-10).

### 4. Creating Personalized Anime Recommendations
- **Analysis**: Built a recommendation system using cosine similarity based on anime genres.
- **Results**:
  - Recommendations for **"Kimi no Na wa."** include:
    - **Wind: A Breath of Heart OVA**
    - **Aura: Maryuuin Kouga Saigo no Tatakai**
    - **Kokoro ga Sakebitagatterunda.**
    - **...**

### 5. Visualizing Findings
- **Analysis**: Used PowerBI to create visualizations summarizing the findings.
- **Results**:
  - Visualizations include:
    - Total Ratings by Types
    - Total Animes by Ratings
    - Average Ratings by Genres
    - Total Ratings by Genres
    - Average Ratings by Titles
    - Average Ratings by Types

## Summary
This project provides a comprehensive analysis of anime ratings and user preferences, developing a recommendation system to suggest similar anime. The findings and visualizations in PowerBI offer valuable insights into the anime landscape, assisting users in discovering new anime.