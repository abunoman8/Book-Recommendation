class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.ratings = []
        self.reviews = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            print(f"Rating of {rating} added for '{self.title}'")
        else:
            print("Invalid rating. Please rate between 1 and 5.")

    def add_review(self, review):
        self.reviews.append(review)
        print(f"Review added for '{self.title}'")

    def average_rating(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0.0

    def ___str__(self):
        return f"'{self.title}' by {self.author} [Genre: {self.genre}] (Average Rating: {self.average_rating():.2f})"


class BookRecommendationSystem:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, genre):
        book = Book(title, author, genre)
        self.books.append(book)

    def suggest_books_by_genre(self, genre):
        suggestions = [book for book in self.books if book.genre.lower() == genre.lower()]
        if suggestions:
            print(f"\nBooks in the genre '{genre}':")
            for book in suggestions:
                print(book)
        else:
            print(f"No books found in the genre '{genre}'.")

    def suggest_books_by_author(self, author):
        suggestions = [book for book in self.books if book.author.lower() == author.lower()]
        if suggestions:
            print(f"\nBooks by '{author}':")
            for book in suggestions:
                print(book)
        else:
            print(f"No books found by '{author}'.")

    def rate_and_review_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                try:
                    rating = int(input(f"Rate '{book.title}' (1-5): "))
                    book.add_rating(rating)
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
                review = input(f"Write a review for '{book.title}': ")
                book.add_review(review)
                return
        print(f"No book found with the title '{title}'.")


# Example Usage
if __name__ == "__main__":
    system = BookRecommendationSystem()
    
    # Adding books
    system.add_book("To Kill a Mockingbird", "Harper Lee", "Fiction")
    system.add_book("1984", "George Orwell", "Dystopian")
    system.add_book("Pride and Prejudice", "Jane Austen", "Romance")
    
    # Suggesting books
    system.suggest_books_by_genre("Fiction")
    system.suggest_books_by_author("Jane Austen")
    
    # Rating and reviewing a book
    system.rate_and_review_book("1984")