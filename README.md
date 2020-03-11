# Hospital Appointment Queue
A dockerized application for queuing patients according to severity of the diseases.

### High level requirements

*   Use at least 3 different disease types.
*   Accept at least 3 patients who have different diseases.
*   Ensure system holds the records of cured patients informations.
*   Assign an unique identifier to each patient and save these patients' data periodically.

### Technical requirements

*   Use RabbitMQ as a message broker.
*   Use a NoSQL database such as MongoDB.
*   Use Python version 3.6+.
*   Use docker for containerization.