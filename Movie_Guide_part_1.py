using System;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        // Prepopulate movie list
        List<string> movies = InitializeMovieList();
        
        // Display menu and process user choices
        while (true)
        {
            DisplayMenu();
            Console.Write("\nEnter your choice: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    DisplayMovies(movies);
                    break;
                case "2":
                    AddMovie(movies);
                    break;
                case "3":
                    RemoveMovie(movies);
                    break;
                case "4":
                    Console.WriteLine("Exiting program...");
                    return;
                default:
                    Console.WriteLine("Invalid option. Please enter a number between 1-4.");
                    break;
            }
        }
    }

    static void DisplayMenu()
    {
        Console.WriteLine("\nMovie Guide");
        Console.WriteLine("1. View Movies");
        Console.WriteLine("2. Add Movie");
        Console.WriteLine("3. Remove Movie");
        Console.WriteLine("4. Exit");
    }

    static List<string> InitializeMovieList()
    {
        return new List<string> { "Inception", "The Matrix", "Interstellar" };
    }

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
