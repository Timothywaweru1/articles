from models.author import Author
from models.magazine import Magazine
from models.article import Article

def seed_database():
    author1 = Author(name="Peter").save()
    author2 = Author(name="Lara Croft").save()
    author3 = Author(name="Bob Oketch").save()

    mag1 = Magazine(name="Tech Today", category="Technology").save()
    mag2 = Magazine(name="Science Weekly", category="Science").save()
    mag3 = Magazine(name="Business Insights", category="Business").save()

Article(title="Understanding Python Internals", author_id=author1.id, magazine_id=mag1.id).save()
Article(title="The Future of Artificial Intelligence", author_id=author1.id, magazine_id=mag1.id).save()
Article(title="Getting Started with Machine Learning", author_id=author1.id, magazine_id=mag1.id).save()
Article(title="Exploring Quantum Realms", author_id=author2.id, magazine_id=mag2.id).save()
Article(title="Breakthroughs in Brain Science", author_id=author2.id, magazine_id=mag2.id).save()
Article(title="Analyzing Economic Shifts", author_id=author3.id, magazine_id=mag3.id).save()
Article(title="Building Successful Startups", author_id=author3.id, magazine_id=mag3.id).save()
Article(title="Smart Financial Choices", author_id=author3.id, magazine_id=mag3.id).save()
Article(title="Decoding the Blockchain", author_id=author1.id, magazine_id=mag3.id).save()

print("Database seeded successfully!")