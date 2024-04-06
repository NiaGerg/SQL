import sqlite3
import random


def create_database():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Book (
                name TEXT,
                num_pages INTEGER,
                cover_type TEXT,
                category TEXT
             )''')
    conn.commit()
    conn.close()


def generate_books(num_entries=10):
    categories = ['Fiction', 'Thriller', 'Science Fiction', 'Biography', 'History']
    cover_types = ['Hardcover', 'Paperback', 'Ebook']
    with sqlite3.connect('books.db') as conn:
        c = conn.cursor()
        create_database()
        for _ in range(num_entries):
            name = f"Book {random.randint(1, 100)}"
            num_pages = random.randint(100, 500)
            cover_type = random.choice(cover_types)
            category = random.choice(categories)
            c.execute("INSERT INTO Book VALUES (?, ?, ?, ?)", (name, num_pages, cover_type, category))
        conn.commit()


def get_average_pages():
    with sqlite3.connect('books.db') as conn:
        c = conn.cursor()
        c.execute("SELECT AVG(num_pages) FROM Book")
        avg_pages = c.fetchone()[0]
        print(f"Average number of pages: {avg_pages:.2f}")


def get_largest_book():
    with sqlite3.connect('books.db') as conn:
        c = conn.cursor()
        c.execute("SELECT name, num_pages FROM Book ORDER BY num_pages DESC LIMIT 1")
        largest_book = c.fetchone()
        if largest_book:
            print(f"Largest book: {largest_book[0]} ({largest_book[1]} pages)")
        else:
            print("No books found in the database.")


if __name__ == "__main__":
    generate_books()
    get_average_pages()
    get_largest_book()
    