import pandas as pd
import sqlite3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import messagebox, ttk

# Load the dataset
anime = pd.read_csv('anime.csv')

# Fill missing values
anime['genre'].fillna('Unknown', inplace=True)
anime['type'].fillna(anime['type'].mode()[0], inplace=True)
anime['rating'].fillna(anime['rating'].mean(), inplace=True)

# Create a lowercase version of the anime names for case-insensitive comparison
anime['name_lower'] = anime['name'].str.lower()

# Connect to SQLite database
conn = sqlite3.connect('anime_recommendations.db')
c = conn.cursor()

# Create table
c.execute('''
CREATE TABLE IF NOT EXISTS anime (
    anime_id INTEGER PRIMARY KEY,
    name TEXT,
    name_lower TEXT,
    genre TEXT,
    type TEXT,
    episodes INTEGER,
    rating REAL,
    members INTEGER
)
''')

# Insert data into the table
anime.to_sql('anime', conn, if_exists='replace', index=False)

# Commit and close connection
conn.commit()

# Recommendation function
def get_recommendations(title, n_recommendations=10):
    # Convert the input title to lowercase for case-insensitive comparison
    title_lower = title.lower()
    
    # Load data from the anime table
    anime = pd.read_sql_query("SELECT * FROM anime", conn)
    
    # Create a count matrix for the 'genre' column
    count_vectorizer = CountVectorizer(tokenizer=lambda x: x.split(', '))
    genre_matrix = count_vectorizer.fit_transform(anime['genre'].fillna(''))

    # Compute the cosine similarity based on the count matrix
    cosine_sim = cosine_similarity(genre_matrix, genre_matrix)
    
    # Get the index of the anime that matches the title
    idx = anime[anime['name_lower'] == title_lower].index[0]

    # Get the pairwise similarity scores of all anime with that anime
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the anime based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the top n most similar anime
    sim_scores = sim_scores[1:n_recommendations + 1]

    # Get the anime indices
    anime_indices = [i[0] for i in sim_scores]

    # Return the top n most similar anime
    return anime[['name', 'genre', 'rating']].iloc[anime_indices]

# GUI
def show_recommendations(event=None):
    title = entry.get()
    if not title:
        messagebox.showerror("Input Error", "Please enter an anime name")
        return
    
    try:
        recommendations = get_recommendations(title)
    except IndexError:
        messagebox.showerror("Input Error", "Anime not found in the database")
        return
    
    for i in tree.get_children():
        tree.delete(i)
    
    for i, row in recommendations.iterrows():
        tree.insert("", "end", values=(row['name'], row['genre'], f"{row['rating']:.2f}"))

# Create the main window
root = tk.Tk()
root.title("Anime Recommendation System")
root.configure(background="#FFFFFF")

# Set the style
style = ttk.Style(root)
style.theme_use("clam")

# Configure the styles for widgets
style.configure("TLabel", background="#FFFFFF", foreground="#002b58", font=("Consolas", 12, "bold"))
style.configure("TButton", background="#b2d7fe", foreground="#002b58", font=("Consolas", 12))
style.configure("TEntry", fieldbackground="#FFFFFF", foreground="#002b58", font=("Consolas", 12))
style.configure("Treeview", background="#eaf4fe", foreground="#002b58", font=("Consolas", 12), rowheight=25)
style.configure("Treeview.Heading", background="#b2d7fe", foreground="#002b58", font=("Consolas", 12, "bold"))

# Create and place the widgets
ttk.Label(root, text="Enter Anime Name:").pack(pady=10)
entry = ttk.Entry(root, width=50)
entry.pack(pady=10)
entry.bind("<Return>", show_recommendations)  # Bind Enter key to show_recommendations function

ttk.Button(root, text="Get Recommendations", command=show_recommendations).pack(pady=10)

# Create a Treeview widget
columns = ("Name", "Genre", "Rating")
tree = ttk.Treeview(root, columns=columns, show="headings", height=10)
tree.heading("Name", text="Name")
tree.heading("Genre", text="Genre")
tree.heading("Rating", text="Rating")

# Adjust column widths
tree.column("Name", width=200)
tree.column("Genre", width=400)
tree.column("Rating", width=100)

tree.pack(pady=10, fill=tk.BOTH, expand=True)

# Apply style to Treeview widget
style.map('Treeview', background=[('selected', '#b2d7fe')])

# Run the application
root.mainloop()

# Close the SQLite connection
conn.close()
