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

    static void DisplayMovies(List<string> movies)
    {
        Console.WriteLine("\nMovie List:");
        for (int i = 0; i < movies.Count; i++)
        {
            Console.WriteLine($"{i + 1}. {movies[i]}");
        }
    }

    static void AddMovie(List<string> movies)
    {
        Console.Write("\nEnter movie name to add: ");
        string newMovie = Console.ReadLine();
        movies.Add(newMovie);
        Console.WriteLine($"'{newMovie}' added to the list.");
        DisplayMovies(movies);
    }

    static void RemoveMovie(List<string> movies)
    {
        DisplayMovies(movies);
        Console.Write("\nEnter the number of the movie to remove: ");
        
        if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= movies.Count)
        {
            Console.WriteLine($"Removing '{movies[index - 1]}'...");
            movies.RemoveAt(index - 1);
            DisplayMovies(movies);
        }
        else
        {
            Console.WriteLine("Invalid number. Please enter a valid movie number.");
        }
    }
}
