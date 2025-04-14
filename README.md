# Hotel Booking Analytics with Chatbot

This project provides an interactive hotel booking analytics system with a user-friendly UI and a chatbot feature. The application analyzes hotel booking data, answers user queries about the data, and displays analytics visualizations.

The system is built using **Flask** for the backend and **HTML/CSS** for the frontend.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Folder Structure](#folder-structure)
- [Frontend UI Setup](#frontend-ui-setup)
  - [index.html](#indexhtml)
  - [style.css](#stylecss)
- [Backend Setup](#backend-setup)
- [Endpoints](#endpoints)
  - [GET /analytics](#get-analytics)
  - [POST /chat](#post-chat)
- [Setup and Installation](#setup-and-installation)
- [Running the Application](#running-the-application)
- [License](#license)

## Project Overview

This project provides a web interface to interact with hotel booking analytics data and ask questions using a chatbot. The backend handles requests and serves data, while the frontend provides a clean, easy-to-use interface. Users can view analytics and ask specific questions regarding booking trends and customer data.

---

## Technologies Used

- **Python**: For backend development.
- **Flask**: Web framework for serving the application.
- **HTML/CSS**: For building the user interface.
- **JavaScript**: To handle frontend interactions.
- **Pandas**: For data manipulation and analysis.
- **Chroma**: Vector store for document embedding and question answering.
- **Flask-CORS**: To handle Cross-Origin Resource Sharing (CORS).
- **Dotenv**: For managing environment variables securely.

---

## Folder Structure
hotel-booking-analytics/ │ ├── app.py ← Flask backend for serving API and chatbot ├── rag.py ← RAG model setup and data processing ├── templates/
│ └── index.html ← Frontend UI page ├── static/
│ └── style.css ← Optional CSS for styling the page ├── .env ← Environment variables └── README.md ← Project overview and instructions


---

## Frontend UI Setup

The frontend consists of an interactive **HTML** page where users can input questions about hotel booking analytics. The page is styled using **CSS** for a clean design.

## Backend Setup

The backend is powered by Flask, which processes HTTP requests and serves data from the analytics and chatbot endpoints. Below are the steps to configure and set up the Flask application.

### **main.py**

This file contains the backend code that powers both the chatbot and the analytics routes.

### running time
![Screenshot 2025-04-14 223124](https://github.com/user-attachments/assets/e02f0668-7a9d-4db4-94ef-2cf76c2f9235)


--- 

### INTERFACE
![BASIC INTRO](https://github.com/user-attachments/assets/c074f526-c698-4f2b-832c-f6ade5f15285)

### QUESTION
![Screenshot 2025-04-14 223101](https://github.com/user-attachments/assets/69f2c6b6-553d-4f04-84ee-c5f9e6fa1d0c)





