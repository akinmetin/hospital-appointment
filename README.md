# Hospital Appointment Queue
A dockerized application for queuing patients according to severity of the disease.

### High level requirements

*   Use at least 4 different diseases.
*   Accept at least 3 patients who have different diseases at every hour between 8 am. and 5 pm.
*   Ensure system holds the informations of all patients.

### Technical requirements

*   Use RabbitMQ as a message broker.
*   Use a NoSQL database such as MongoDB.
*   Use Python version 3.6+.
*   Use docker for containerization.