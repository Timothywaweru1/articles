from lib.models.author import Author
from lib.models.magazine import Magazine

def seed_data():
    a1 = Author("TIMOTHY")
    a1.save()
    a2 = Author("FRANCIS")
    a2.save()

    m1 = Magazine("CARWOW", "Super cars")
    m1.save()
    m2 = Magazine("SHUJAA", "Comedy")
    m2.save()

    a1.add_article(m1, "Electric Cars")
    a1.add_article(m2, "Construction")
    a2.add_article(m2, "Power")

if __name__ == "__main__":
    seed_data()