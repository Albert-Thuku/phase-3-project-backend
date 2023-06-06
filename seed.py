from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Users, Destinations
import random
from faker import Faker
if __name__=='__main__':
    engine = create_engine('sqlite:///project.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Users).delete()
    session.query(Destinations).delete()

    fake = Faker()

    destination_names = ['Hala Park', 'Diani Beach', 'Nairobi National Museum', 'Tsavo Park', 'Milan', 'Park Inn']
    categories = ['Hotel', 'National Park', 'Sandy Beach', 'Museum', 'Water Park', 'Restaurant']
    locations = ['Nairobi', 'Mombasa', 'Kilifi', 'Tsavo East', 'Westlands', 'Malindi']

    users = []
    for i in range(6):
        user = Users(
            name = fake.unique.name(),
            password = fake.unique.password()
        )

        session.add(user)
        session.commit()
        users.append(user)

    destinations = []
    for i in range(6):
        destination = Destinations(
            name = random.choice(destination_names),
            image = fake.unique.url(),
            description = fake.unique.sentence(),
            category = random.choice(categories),
            location = random.choice(locations),
            visit_url = fake.unique.url(),
            interested = False,
            user_id = random.randint(1,7)
        )

        session.add(destination)
        session.commit()
        destinations.append(destination)

    session.bulk_save_objects(destinations)
    session.commit()
    session.close()