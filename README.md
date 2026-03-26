# MCDA 5550 - Hotel Reservation REST API

This is a REST API developed using Django REST Framework for a Hotel Reservation System. It handles queries for available hotels and creates reservations alongside associated guest details.

## Project Setup Instructions

Follow these instructions to run the application locally for testing:

1. **Prerequisites**: Ensure you have Python installed.
2. **Create/Activate Virtual Environment (Optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install django djangorestframework
   ```
4. **Database Migrations** (The built-in SQLite database is pre-configured, but to ensure it is up-to-date, run):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```
   The API will be accessible at `http://127.0.0.1:8000/`.

## API Keys & Authentication
No API keys, headers, or authentication credentials are required to interact with this application. The API requests are open for direct testing via Postman or Any REST Client.

## API Documentation

### 1. Get List of Hotels
- **Function Name**: `getListOfHotels`
- **HTTP Method**: `GET`
- **URL Endpoint**: `http://127.0.0.1:8000/api/getListOfHotels`
- **Description**: Returns the list of hotels available in the system. The listing changes dynamically based on the presence/absence of check-in parameters.
- **Example Usage** (Postman / Browser / cURL):
  ```bash
  curl -X GET "http://127.0.0.1:8000/api/getListOfHotels?checkin=2026-12-01&checkout=2026-12-05"
  ```
- **Sample Success Response**:
  ```json
  {
      "hotels": [
          {
              "hotel_name": "City Center Inn",
              "price_per_night": 100,
              "location": "New York"
          },
          {
              "hotel_name": "Airport Tracker Hotel",
              "price_per_night": 80,
              "location": "Chicago"
          }
      ]
  }
  ```

### 2. Create Reservation Confirmation
- **Function Name**: `reservationConfirmation`
- **HTTP Method**: `POST`
- **URL Endpoint**: `http://127.0.0.1:8000/api/reservationConfirmation`
- **Description**: Submits guest names alongside their desired hotel/dates. All guests are safely and explicitly tied to the underlying Reservation database entry using Foreign Keys.
- **Sample Request Body** (`application/json`):
  ```json
  {
      "hotel_name": "City Center Inn",
      "checkin": "2026-12-01",
      "checkout": "2026-12-05",
      "guests_list": [
          {
              "guest_name": "John Doe",
              "gender": "Male"
          },
          {
              "guest_name": "Jane Doe",
              "gender": "Female"
          }
      ]
  }
  ```
- **Sample Success Response**: 
  Upon successful creation, returns a unique 8-character alphanumeric confirmation number.
  ```json
  {
      "confirmation_number": "A9B2K5PQ"
  }
  ```
