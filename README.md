# Hospital Appointment Queue
A dockerized application for queuing patients according to severity of the diseases.

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f6ba5cd4523742a3bd4a502774ccbe54)](https://www.codacy.com/manual/metin_akin_bursa/hospital-appointment?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=akinmetin/hospital-appointment&amp;utm_campaign=Badge_Grade)

## Getting Started

These instructions will get you a copy of the project up and running on a docker container for development and testing purposes.

### Prerequisites

``Docker``

### High level requirements

*   Use at least 3 different disease types.
*   Accept at least 3 patients who have different diseases.
*   Ensure system holds the records of cured patients informations.
*   Save each patient's data periodically (on every 50 patients).

### Technical requirements

*   Use RabbitMQ as a message broker.
*   Use a NoSQL database such as MongoDB.
*   Use Python version 3.6+.
*   Use docker for containerization.

### Installing

*   Download this repository and extract it to any folder.

*   Build it using ``docker-compose build`` and run it using ``docker-compose up -d``.

*   You need to run this command to add items into the RabbitMQ queue using: ``docker-compose run app python emergency_service.py``.

*   Create an ``.env`` file for environmental variables.

*   Environmental Variables
    *   ``DB_USER``: Database username for the MongoDB server.
    *   ``DB_PASSWORD``: Database password for the MongoDB server.
    *   ``DB_HOST``: Hostname or IP of the MongoDB server.
    *   ``DB_PORT``: Port of the MongoDB server.
    *   ``RABBITMQ_DEFAULT_USER``: RabbitMQ root username.
    *   ``RABBITMQ_DEFAULT_PASS``: RabbitMQ root password.

## Versioning

| Version       | Date            | Changes                                       |
| ------------- |:---------------:|:--------------------------------------------- |
| v1.0.0        | 06/03/2020      | Initial development                           |
| v1.1.0        | 11/03/2020      | MongoDB added and cleaned the code            |

### Licensing

All types usage of this project is required permission from owner of the repository.