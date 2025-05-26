from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

if __name__ == "__main__":

    tim = Author("Waweru Timothy")
    alex.save()

    mag = Magazine("CarWow", "Cars")
    mag.save()

    article = tim.add_article(mag, "Neo c")

    print("Author's Magazines:", tim.magazines())
    print("Author's Topics:", tim.topic_areas())
    
    print(f"Article saved: {article.title}")