# Timetable Viewer and Generator

#### Video Demo: "https://youtu.be/hprFVNMz9Q0"

#### Description:

# Purpose

The purpose of the program is to allow the uses to upload raw dataset( Timetable ), which are in csv format to the program. The user can then search and sort the timetable based on certain criteria and export it in excel file.

# More Details

A Timetable Viewer and Generator is a software application designed to help users create, manage, and view schedules or timetables for various purposes, such as academic schedules for schools and universities, work shifts for businesses, event scheduling, and more. This type of software typically includes a database to store information about events, resources, and users, and it provides a user-friendly interface for creating, editing, and viewing timetables. Here's an overview of the project and the database structure for a Timetable Viewer and Generator:

Project Overview:
The project aims to create a user-friendly application that allows users to:

Create Timetables: Users can define the structure of their timetables, specifying details like time slots, days of the week, and the type of activities or events to schedule.

Add Events/Resources: Users can add events, classes, or activities to the timetable. Each event typically includes information like a title, description, location, start time, end time, and any associated resources.

View Timetables: Users can view their timetables, which display all scheduled events in a clear and organized format.

Generate Timetables: The system can automatically generate timetables based on user-defined constraints and preferences, such as room availability, teacher availability, and avoiding scheduling conflicts.

User Management: There may be user accounts with different roles, such as administrators, teachers, and students. Users can log in, save their timetables, and manage their schedules.

Database Structure:
To support the functionality of the Timetable Viewer and Generator, you would need a database to store and manage various data elements. Here's a simplified database structure:

User Table:

User ID (Primary Key)
Username
Password (hashed and salted)
Role (e.g., admin, teacher, student)
Event Table:

Event ID (Primary Key)
Title
Description
Location
Start Time
End Time
Assigned User (Teacher or Organizer)
Other event-specific attributes
Timetable Table:

Timetable ID (Primary Key)
User ID (Foreign Key referencing the User table)
Timetable Name
Timetable Description
Other timetable-specific attributes
Timetable Event Table (Many-to-Many Relationship):

Timetable Event ID (Primary Key)
Timetable ID (Foreign Key referencing the Timetable table)
Event ID (Foreign Key referencing the Event table)
Day of the week
Time Slot
Other scheduling-specific attributes
Resource Table:

Resource ID (Primary Key)
Resource Name
Description
Availability
Location
Other resource-specific attributes
This database structure allows you to store information about users, events, timetables, and resources. The Timetable Event table facilitates the association of events with specific timetables, allowing users to schedule events on their timetables. The resource table is useful for managing and assigning resources to events, such as classrooms or equipment.

The project would involve creating a web or desktop application with a user interface for interacting with this database, allowing users to create, manage, view, and generate timetables based on their specific needs and preferences. The database stores the data needed for the application to function effectively.


# Data Structures

A list of dictionaries is a flexible data structure in Python for storing structured data. Each dictionary in the list represents a data record, with keys corresponding to attributes. For a Timetable Viewer and Generator, you can use this structure to store event data, where each dictionary holds information such as event title, description, location, start and end times, and assigned users. This approach allows you to easily add, update, and access event data within the list, making it a convenient choice for managing and manipulating information in your application. You can apply a similar structure to other data entities like users, timetables, and resources, using separate lists of dictionaries for each entity.

# Algorithms

Linear Search:

Linear search is a simple search algorithm used to find a specific element within a collection of data, such as an array or list. It works by examining each element in the collection one by one until a match is found or until the entire collection has been searched. Here's how linear search is used:

Searching for an Element: Linear search is used when you want to find a particular element in a dataset. It starts at the beginning of the data and iterates through each element until it either finds a match or reaches the end of the data.

Merge Sort:

Merge sort is a comparison-based sorting algorithm that divides an array into two halves, sorts each half, and then merges them to produce a sorted array. It is often used for efficient and stable sorting of larger datasets. Here's how merge sort is used:

Sorting an Array: Merge sort is used when you need to sort an array or a list in ascending or descending order. It is a divide-and-conquer algorithm that recursively divides the input array until it reaches base cases (usually arrays of size 1), and then merges the smaller sorted arrays back together.

# Libraries

Pandas and tabulate are used as main libraries to process, load and display the data in a tabular format.

# Object-Oriented Programming

Dataset class mainly loads and process the files while database handles the main features of the program like searching and sorting. Lastly, Menu class interacts with the user.

:3
