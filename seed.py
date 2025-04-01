import sys
from pathlib import Path
from dotenv import load_dotenv

# Adiciona o diretório 'src' ao PATH para permitir importações corretas
sys.path.append(str(Path(__file__).parent / "src"))

# Carrega variáveis do .env antes de importar outros módulos
load_dotenv()

from sqlalchemy.orm import Session
from app.db.base import Base, engine
from app.models import Customer, Mechanic, Part, Vehicle, ServiceOrder, ServiceItem
from faker import Faker
import random

fake = Faker("pt_BR")

def seed_database():
    # Cria todas as tabelas (se não existirem)
    Base.metadata.create_all(bind=engine)

    with Session(engine) as session:
        # ========== CRIAR CLIENTES ==========
        customers = []
        for _ in range(5):
            customer = Customer(
                name=fake.name(),
                cpf=fake.cpf(),
                phone=fake.numerify(text="(##) #####-####"),
                email=fake.user_name() + "@example.com",
                address=fake.address()
            )
            customers.append(customer)
        session.add_all(customers)
        session.flush()  # Gera IDs dos clientes

        # ========== CRIAR MECÂNICOS ==========
        mechanics = []
        specialties = ["Motor", "Freios", "Elétrica", "Suspensão", "Injeção Eletrônica"]
        for _ in range(3):
            mechanic = Mechanic(
                name=fake.name(),
                specialty=random.choice(specialties),
                phone=fake.phone_number(),
                available=fake.boolean()
            )
            mechanics.append(mechanic)
        session.add_all(mechanics)
        session.flush()  # Gera IDs dos mecânicos

        # ========== CRIAR PEÇAS ==========
        parts = []
        part_names = ["Vela de Ignição", "Pastilha de Freio", "Filtro de Ar", "Amortecedor", "Sensor de Oxigênio"]
        for name in part_names:
            part = Part(
                name=name,
                code=fake.unique.bothify(text="PART-#####"),
                stock_quantity=random.randint(10, 100),
                cost_price=round(random.uniform(50, 500), 2),
                selling_price=round(random.uniform(100, 1000), 2)
            )
            parts.append(part)
        session.add_all(parts)

        # ========== CRIAR VEÍCULOS ==========
        vehicles = []
        brands = ["Toyota", "Volkswagen", "Ford", "Chevrolet", "Honda"]
        for customer in customers:
            vehicle = Vehicle(
                license_plate=fake.bothify(text="???-####").upper(),
                brand=random.choice(brands),
                model=fake.word().capitalize(),
                year=random.randint(1980, 2024),
                customer_id=customer.id
            )
            vehicles.append(vehicle)
        session.add_all(vehicles)
        session.flush()  # Gera IDs dos veículos

        # ========== CRIAR ORDENS DE SERVIÇO ==========
        service_orders = []
        statuses = ["PENDING", "IN_PROGRESS", "COMPLETED"]
        for _ in range(10):
            service_order = ServiceOrder(
                vehicle_id=random.choice(vehicles).id,
                mechanic_id=random.choice(mechanics).id,
                status=random.choice(statuses),
                entry_date=fake.date_time_this_year(),
                total_value=0.0
            )
            service_orders.append(service_order)
        session.add_all(service_orders)
        session.flush()

        # ========== CRIAR ITENS DAS ORDENS ==========
        for order in service_orders:
            num_items = random.randint(1, 5)
            total = 0.0
            for _ in range(num_items):
                part = random.choice(parts)
                quantity = random.randint(1, 3)
                unit_value = part.selling_price
                total += unit_value * quantity

                item = ServiceItem(
                    service_order_id=order.id,
                    part_id=part.id,
                    quantity=quantity,
                    unit_value=unit_value,
                    description=f"Troca de {part.name}"
                )
                session.add(item)
            order.total_value = total

        # Commit final para salvar tudo
        session.commit()

if __name__ == "__main__":
    seed_database()
    print("✅ Dados mockados inseridos com sucesso!")