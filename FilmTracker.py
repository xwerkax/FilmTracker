import pandas as pd

file_path = "movies.csv"
movies = pd.read_csv(file_path)

user_ratings = {}
watchlist = []


def get_user_rating():
    movie_id = input("Enter movie ID: ")
    rating = int(input("Rate the movie on a scale from 1 to 5: "))

    if rating < 1 or rating > 5:
        print("Invalid rating. Please enter a number between 1 and 5.")
        return

    user_ratings[movie_id] = rating
    print(f"Rated movie {movie_id} with {rating} stars.")


def add_to_watchlist():
    movie_id = input("Enter movie ID to add to watchlist: ")
    watchlist.append(movie_id)
    print(f"Movie {movie_id} added to your watchlist.")


def view_watchlist():
    if not watchlist:
        print("Your watchlist is empty.")
    else:
        print("Your watchlist:")
        for movie_id in watchlist:
            movie_title = movies.loc[movies["id"].astype(str) == movie_id, "title"].values
            if movie_title:
                print(f"- {movie_title[0]}")
            else:
                print(f"- Movie ID {movie_id} (not found in database)")


def view_ratings():
    if not user_ratings:
        print("You have not rated any movies yet.")
    else:
        print("Your rated movies:")
        for movie_id, rating in user_ratings.items():
            movie_title = movies.loc[movies["id"].astype(str) == movie_id, "title"].values
            if movie_title:
                print(f"- {movie_title[0]}: {rating} stars")
            else:
                print(f"- Movie ID {movie_id}: {rating} stars (not found in database)")


def recommend_movie():
    if not user_ratings:
        print("No ratings yet. Rate a movie first to get recommendations.")
        return

    top_movie_id = max(user_ratings, key=user_ratings.get)
    top_movie_genre = movies.loc[movies["id"].astype(str) == top_movie_id, "genre"].values[0]

    recommendations = movies[movies["genre"] == top_movie_genre]
    recommendations = recommendations[~recommendations["id"].astype(str).isin(user_ratings.keys())]

    if not recommendations.empty:
        recommended_movie = recommendations.sample(1)[["title", "genre"]].values[0]
        print(f"Recommended: {recommended_movie[0]} ({recommended_movie[1]})")
    else:
        print("No recommendations available.")


# Main Program Loop
while True:
    print("\nOptions:")
    print("1. Rate a movie")
    print("2. Add movie to watchlist")
    print("3. View watchlist")
    print("4. View rated movies")
    print("5. Get a recommendation")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        get_user_rating()
    elif choice == "2":
        add_to_watchlist()
    elif choice == "3":
        view_watchlist()
    elif choice == "4":
        view_ratings()
    elif choice == "5":
        recommend_movie()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
