# Mechanical Workshop System

A complete system for managing service orders in mechanical workshops, developed with FastAPI and SQLAlchemy. The system allows efficient management of customers, vehicles, services, and inventory, offering a modern and well-documented REST API interface.

## 🚀 Features

### Customer Management
- Complete customer registration with contact information
- Service history by customer
- Management of multiple vehicles per customer

### Vehicle Control
- Detailed vehicle registration (make, model, year, license plate)
- Complete maintenance history
- Preventive maintenance alerts

### Service Orders
- Creation and tracking of service orders
- Assignment of mechanics
- Registration of parts used
- Real-time service status
- Quotes and approvals

### Mechanics Management
- Registration of mechanics and their specialties
- Availability control
- History of services performed

### Inventory Control
- Parts and materials management
- Input and output control
- Low stock alerts
- Integration with service orders

### Reports and Analytics
- Management dashboard
- Billing reports
- Efficiency analysis by mechanic
- Service history by vehicle

## 🛠️ Technologies Used

- **FastAPI**: Modern framework for building APIs with Python
- **SQLAlchemy**: ORM for database interaction
- **PostgreSQL**: Relational database
- **Pydantic**: Data validation and serialization
- **Alembic**: Database migration control
- **JWT**: Authentication and authorization
- **Docker**: Application containerization

## 📦 Project Structure

```
mechanical-workshop-system/
├── alembic/
│   └── versions/
├── app/
│   ├── api/
│   │   └── v1/
│   ├── core/
│   ├── crud/
│   ├── db/
│   ├── models/
│   └── schemas/
├── tests/
├── .env
├── docker-compose.yml
└── requirements.txt
```

## 🚀 How to Run the Project

1. Clone the repository
```bash
git clone https://github.com/your-username/mechanical-workshop-system.git
cd mechanical-workshop-system
```

2. Configure the virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables in the `.env` file

5. Run migrations
```bash
alembic upgrade head
```

6. Start the server
```bash
uvicorn app.main:app --reload
```

## 📚 API Documentation

After starting the server, interactive documentation will be available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🤝 Contributing

1. Fork the project
2. Create a branch for your feature (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is under the MIT license. See the [LICENSE](LICENSE) file for more details.
