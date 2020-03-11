# Hospital Appointment Queue
A dockerized application for queuing patients according to severity of the diseases.
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f6ba5cd4523742a3bd4a502774ccbe54)](https://www.codacy.com/manual/metin_akin_bursa/hospital-appointment?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=akinmetin/hospital-appointment&amp;utm_campaign=Badge_Grade)

## Getting Started

These instructions will get you a copy of the project up and running on a docker container for development and testing purposes.

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

### Licensing

All types usage of this project is required permission from owner of the repository.