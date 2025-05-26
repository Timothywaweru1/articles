from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

if __name__ == "__main__":

    alex = Author("Waweru Timothy")
    alex.save()

    mag = Magazine("CarWow", "Cars")
    mag.save()

    article = alex.add_article(mag, "Neo colonialism")
    print(f"Article saved: {article.title}")

    print("Author's Magazines:", alex.magazines())
    print("Author's Topics:", alex.topic_areas())