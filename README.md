# Multithreaded Flask Dashboard

## Overview
This project is a lightweight Flask-based web application designed to demonstrate concurrent data generation using multithreading in Python. The system continuously generates random numbers across multiple predefined ranges, each operating at distinct refresh intervals, and visualizes them in a dynamically updating web dashboard.

The application models independent asynchronous processes and integrates them with a client-facing interface using a simple REST-based architecture.

---

## Demo Video
A demonstration of the application can be viewed here:



---

## Key Features
- Concurrent data generation using multiple threads
- Independent refresh intervals for each data stream
- Real-time dashboard updates without page reload
- Clear separation of backend processing and frontend visualization
- Minimal and efficient system design for demonstration purposes

---

## Motivation for Multithreading
The core requirement of this application is to simulate multiple independent processes that update at different time intervals. Implementing this sequentially would introduce blocking behavior, where one task delays the execution of others.

Multithreading addresses this limitation by enabling parallel execution of tasks within a single process. Each thread operates independently, allowing:
- Asynchronous updates of multiple data streams
- Improved responsiveness of the system
- Accurate simulation of real-time concurrent processes

---

## System Architecture

### Backend (Flask + Threading)
- Initializes and manages multiple worker threads
- Maintains a shared in-memory data structure
- Exposes a REST endpoint (`/data`) for retrieving current values

### Frontend (HTML, CSS, JavaScript)
- Periodically fetches data from the backend using HTTP requests
- Updates the user interface dynamically without reloading the page

---

## Project Structure
