from db.seed import seed_database
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def debug_session():
    # Setup database and seed data
    seed_database()
    
    # Start interactive session
    print("Debug session started. You can now interact with the models.")
    print("Example usage:")
    print("  - author = Author.find_by_id(1)")
    print("  - magazine = Magazine.find_by_name('Tech Today')")
    print("  - articles = Article.find_by_author(1)")

if __name__ == '__main__':
    debug_session()