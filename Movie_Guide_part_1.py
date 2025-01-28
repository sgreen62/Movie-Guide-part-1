# Shawn Green
# CIS261
# Movie Guide Part 1

def display_menu():
    print("\nMovie Guide")
    print("1. View Movies")
    print("2. Add Movie")
    print("3. Remove Movie")
    print("4. Exit")

def initialize_movie_list():
    return ["Inception", "The Matrix", "Interstellar"]

def display_movies(movies):
    if not movies:
        print("\nNo movies in the list.")
        return
    print("\nMovie List:")
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")

def add_movie(movies):
    new_movie = input("\nEnter movie name to add: ")
    if new_movie.strip():
        movies.append(new_movie)
        print(f"'{new_movie}' added to the list.")
    else:
        print("Movie name cannot be empty.")
    display_movies(movies)

def remove_movie(movies):
    display_movies(movies)
    try:
        index = int(input("\nEnter the number of the movie to remove: "))
        if 1 <= index <= len(movies):
            print(f"Removing '{movies[index - 1]}'...")
            movies.pop(index - 1)
        else:
            print("Invalid number. Please enter a valid movie number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    display_movies(movies)

def movie_guide():
    movies = initialize_movie_list()
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            display_movies(movies)
        elif choice == "2":
            add_movie(movies)
        elif choice == "3":
            remove_movie(movies)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please enter a number between 1-4.")

# Run the movie guide
movie_guide()