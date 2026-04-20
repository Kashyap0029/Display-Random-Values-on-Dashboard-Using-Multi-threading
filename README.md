# Display-Random-Values-on-Dashboard-Using-Multi-threading
A Flask-based real-time dashboard that uses multithreading to generate random numbers in different ranges, each updating at independent time intervals, and displays them dynamically on a web interface.
# Multithreaded Flask Dashboard

## Overview
This project is a Flask-based web application that demonstrates the use of multithreading to generate and display real-time data. The application continuously produces random numbers across multiple predefined ranges, each updated at different time intervals, and visualizes them in a dynamic dashboard.

The system simulates concurrent data generation and provides a simple interface to observe how independent processes operate simultaneously in a web environment.

---

## Objectives
- To demonstrate the concept of multithreading in Python
- To simulate concurrent data generation with different execution intervals
- To integrate backend processing with a real-time web interface
- To build a lightweight dashboard using Flask

---

## Features
- Real-time updating dashboard
- Six independent data streams
- Each stream operates with:
  - A unique numeric range
  - A distinct refresh interval
- Clean and structured web interface
- Backend implemented using Flask
- Concurrent execution using Python threading

---

## Why Multithreading is Used
Multithreading is used to allow multiple tasks to run concurrently within the same application. In this project, each data stream is handled by a separate thread.

Each thread:
- Generates random numbers within a specified range
- Updates its assigned position in shared memory
- Operates at its own refresh interval

Without multithreading, these tasks would execute sequentially, causing delays and preventing independent updates. Multithreading ensures that all data streams are updated asynchronously, improving responsiveness and accurately simulating real-time systems.

---

## System Architecture

### Backend (Flask)
- Runs multiple threads
- Maintains shared data structure
- Provides API endpoint (`/data`) to serve current values

### Frontend (HTML, CSS, JavaScript)
- Requests data periodically from the backend
- Updates the dashboard dynamically without page reload
