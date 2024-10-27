
# Apna Hostel Management System

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [System Overview](#system-overview)
- [Database Structure](#database-structure)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Description
The **Apna Hostel Management System** is a console-based application built to simplify hostel administration tasks. The system supports student admissions, provides a secure login interface for students and admins, and enables streamlined room management. Designed with Python and MongoDB, it is a robust solution for administrators seeking an organized, efficient, and scalable system to handle student and room information.

The system leverages MongoDB for its NoSQL capabilities, making data storage and retrieval seamless and flexible. The console interface is designed to be intuitive, allowing users to navigate easily through various options.

---

## Features

### Core Features
- **Student Admission and Room Assignment**: Allows admins to add new students and assign them to rooms dynamically, generating unique room numbers.
- **Secure Login System**:
  - **Students** can log in to view personal details and room assignments.
  - **Admins** have access to view and manage all student and room data.
- **Student Details Management**:
  - Displays comprehensive student information, including personal details and course-related info.
  - Logs each student’s login activities for better tracking.
- **Fee Structure Information**: Shows complete hostel fee details to keep students informed of financial obligations.
- **Admin Dashboard**:
  - Provides admins with full access to add, update, and remove student records.
  - Allows for complete room and student management.

### Additional Features
- **Course Overview**: Details courses available for students based on their academic streams (Science, Commerce, Arts).
- **Logging and Tracking**: Logs student login activities, including time and access attempts, for better record-keeping.
- **Scalable Database Integration**: Utilizes MongoDB’s flexibility to expand data management as the hostel grows.

---

## Technologies Used
- **Python**: The core language for application functionality.
- **MongoDB**: NoSQL database for storing student details, room allocations, and logs.
- **Pandas**: For data manipulation and handling MongoDB data efficiently.
- **PrettyTable**: Displays data in an organized table format in the console.

---

## Installation

### Prerequisites
Ensure the following are installed on your system:
- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **MongoDB**: [Download MongoDB](https://www.mongodb.com/try/download/community)
- **Pip**: Comes with Python and is used to install necessary libraries.

### Setup Instructions

1. **Clone the Repository**  
   Clone the project repository and navigate into the project directory:
   ```bash
   git clone <repository_url>
   cd <project_directory>
   ```

2. **Install Required Libraries**  
   Install the necessary Python libraries:
   ```bash
   pip install pymongo pandas prettytable
   ```

3. **Start MongoDB Server**  
   Make sure MongoDB is running on your system:
   ```bash
   mongod
   ```

4. **Run the Application**  
   Start the main application script:
   ```bash
   python <script_name>.py
   ```

---

## Usage
After launching the system, admins and students will be presented with options in the console interface:

1. **For Admins**:
   - Admins can log in with secure credentials to manage student and room data.
   - The admin dashboard provides options for adding, updating, or removing student records and managing room assignments.

2. **For Students**:
   - Students can log in to view their personal details, room assignments, and fee structure.
   - Students can see courses available based on their stream (Science, Commerce, or Arts).

---

## System Overview
The system operates through a structured command-line interface, offering straightforward prompts for both students and admins. The backend is built to maintain reliable and secure data management.

### User Roles
- **Admin**: Full access to manage student information, room assignments, and logs.
- **Student**: Limited access to view personal details and assigned rooms.

---

## Database Structure
The system utilizes three primary MongoDB collections:
1. **Rooms**: Stores information about each room, including room numbers and availability status.
2. **Student_Details**: Stores each student’s information, such as name, course, room assignment, and fee status.
3. **Student_Logs**: Records each student's login activities for tracking and auditing purposes.

---

## Code Structure
The main application code is divided into functional modules:
- **Admission Module**: Handles student registration and room assignments.
- **Authentication Module**: Manages secure login for both admins and students.
- **Data Display Module**: Provides structured data output in the console using PrettyTable.

---

## Examples
- **Student Admission**: The system prompts the admin for student details and assigns a room number automatically.
- **Login Logs**: The system keeps a timestamped record of each login attempt, stored in the `Student_Logs` collection.
- **Fee Details Display**: Students can access information on fees and payment deadlines.

---

## Contributing
Contributions are welcome! If you’d like to improve the Apna Hostel Management System, feel free to fork the repository and submit a pull request.

### How to Contribute:
1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request with a detailed description of changes.

---

## Future Enhancements
The following features are planned for future releases:
- **Web-Based Interface**: A web-based UI to replace the console application.
- **Automated Fee Reminders**: Integration with email or SMS APIs to send fee reminders.
- **Room Availability Checker**: An automated room allocation system for better efficiency.

---

## License
This project is open-source and available under the MIT License.
