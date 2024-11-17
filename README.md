# WhatPlane ✈️

WhatPlane is a unique app that allows users to identify and track planes flying overhead. Users can "capture" planes, view details, and build their own collection of aircraft. The app integrates a clean and interactive interface with a powerful backend to deliver an engaging user experience.

![image](https://github.com/user-attachments/assets/424a2717-d20d-4663-ad03-4a2adda7aa5e)
![image](https://github.com/user-attachments/assets/d566e1fb-a507-4aad-a9a7-4d23552b87fd)

## Features

### 🚀 Core Functionality
- **Plane Detection:** Identify nearby planes using ADS-B data.
- **Plane Collection:** Collect planes by their type and registration.
- **High Scores:** View global high score, and try to reach the top!

### 🌐 Backend API
- Built with **Django** and **PostgreSQL**.
- Handles:
  - Checking if planes exist in the database.
  - Adding new planes by type and registration.
  - Storing and managing user profiles and plane ownership.

### 🔐 Authentication
- Optional user authentication to personalize the experience:
  - Secure login and token management.
  - User-specific plane collections.

### 🖼️ Visuals
- **Plane Widget:** Displays plane details after adding to the database.
- **Map:** Shows the user's current location.
- **Plane Images:** Displays the most recent photo of the plane that you have captured.

### 🌍 Hosted Solution
- **Frontend:** Flutter app hosted on a DigitalOcean droplet.
- **Backend:** Django API hosted alongside the PostgreSQL database on the same droplet. Accessible via https://whatplane.uk.

## Current Development Focus 🛠️
- Improving the **plane capture functionality** to include plane locations on the map.
- Enhancing the interactive map view.
- Polishing the layout for all devices

## Tech Stack

| Layer        | Technology           |
|--------------|----------------------|
| **Frontend** | Flutter              |
| **Backend**  | Django REST Framework |
| **Database** | PostgreSQL           |
| **Hosting**  | DigitalOcean Droplet |

---

Feel free to contribute or provide feedback to make **WhatPlane** even better! 🛫
