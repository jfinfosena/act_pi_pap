from src.core.database import engine, SessionLocal
from src.users.models import User
from src.products.models import Product
from src.reviews.models import Review
from src.categories.models import Category

# Crear la sesión
db = SessionLocal()

# Insertar categorías
cat1 = Category(name="Bicicletas")
cat2 = Category(name="Accesorios")

db.add_all([cat1, cat2])
db.commit()

# Insertar productos
prod1 = Product(name="Orbea Alma", description="Bicicleta de montaña ligera", category=cat1)
prod2 = Product(name="Orbea Orca", description="Bicicleta de carretera de alto rendimiento", category=cat1)

db.add_all([prod1, prod2])
db.commit()

# Insertar usuarios
user1 = User(username="santiago", email="santi@example.com", hashed_password="hashedpass123")
db.add(user1)
db.commit()

# Insertar reseñas
review1 = Review(rating=5, comment="Excelente bici", user=user1, product=prod1)
review2 = Review(rating=4, comment="Muy buena, pero cara", user=user1, product=prod2)

db.add_all([review1, review2])
db.commit()

db.close()
