# ITUS: Integrated Technology for Urban Sustainability

## Introduction
The Integrated Technology for Urban Sustainability (ITUS) project aims to address the Urban Heat Island (UHI) effect, where urban areas experience higher temperatures than their rural surroundings due to human activities, dense infrastructure, and reduced vegetation. ITUS deploys a network of decentralized sensors to monitor and analyze various environmental parameters such as particulate matter, volatile organic compounds (VOCs), soil moisture, air temperature, humidity, surface temperature, and carbon dioxide levels. Inspired by Greek mythology, ITUS is a guardian of urban environments, providing essential data to combat the UHI effect and promote sustainable urban living.

![ITUS_Blue_1](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/7d7d19b7-54ca-4361-9921-1b31a190ab73)

## Mycelium-Inspired Network
The ITUS project draws inspiration from the mycelium network, a vast underground fungal network that connects plants and trees, facilitating the exchange of nutrients and information. Similarly, ITUS uses a decentralized network of ESP32 microcontrollers communicating via the ESP-NOW protocol. This setup ensures reliable data collection without a single point of failure and allows for effortless scalability as new sensors are added. The ESP-NOW protocol minimizes communication overhead, reduces power consumption, and supports efficient real-time data transmission, mirroring the mycelium network's efficiency in resource distribution.

![Screenshot 2024-05-31 130357](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/b347a5ad-71f9-4dca-afe0-1cea4f142f2f)

## Types of ITUS
### ITUS - Blue: Air Quality Monitor
- **Function:** Monitors urban air quality by measuring particulate matter (PM), VOCs, and other harmful gases.
- **Goal:** Improve city air quality by providing accurate and real-time data for environmental analysis and public health monitoring.

### ITUS - Orange: Temperature Monitor
- **Function:** Monitors urban temperatures, including air and surface temperature.
- **Goal:** Understand and manage urban thermal environments to mitigate the UHI effect.

### ITUS - Brown: Soil and Moisture Monitor
- **Function:** Measures soil moisture levels, temperature, and humidity.
- **Goal:** Manage urban green spaces and agriculture, and understand the impact of soil conditions on the UHI effect.


![Screenshot 2024-05-03 073000](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/69533b64-71a4-4e14-b42d-0cd2f6458a8a)

## ITUS Blue (B1) Prototype
### Design
The ITUS Blue (B1) prototype integrates several key design elements inspired by mushrooms:
- **Cap:** Shields sensors against harsh weather conditions.
- **Stem:** Provides support and houses internal wiring.
- **Sensors:** Equipped with precision sensors for various environmental parameters.
- **ESP32:** Processes data and facilitates communication.
- **Mesh:** Prevents debris from interfering with sensors.
- **Gills:** Enhance airflow and prevent overheating.

### Hardware Components
- **ESP32 Microcontroller:** Central processing unit, handles data conversion and communication.
- **Sensirion SEN5x Sensor Node:** Measures PM, VOCs, NOx, RH, and temperature.
- **12V Power Supply:** Ensures stable operation.
- **3D Printed Filament (PLA Plastic):** Constructs the device’s housing.
- **UV Coating (UV-Resistant Clear Gloss):** Protects the device from UV radiation.

![Screenshot 2024-05-03 064101](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/d53f5f4b-5354-4185-83d1-6a2d2afff01c)

![Screenshot 2024-05-03 064351](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/e6f8ea10-9cbb-436c-b86a-ffc25997ba7a)


### Working of the ITUS Blue (B1) Prototype


![IMG_2634](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/bec5d8d3-c2d2-4437-9959-fc2785c1e4e2)


#### Data Collection
The Sensirion SEN55 sensor node measures multiple environmental parameters, including particulate matter (PM1.0, PM2.5, PM4, PM10), volatile organic compounds (VOCs), nitrogen oxides (NOx), relative humidity (RH), and temperature (T). The sensor uses laser scattering to detect PM and metal oxide semiconductor (MOS) technology to detect VOCs and NOx. Capacitive sensors measure RH, and thermistors measure temperature.

#### Data Processing
The ESP32 microcontroller is responsible for processing the raw data from the SEN55 sensor. It handles the data conversion, ensuring the readings are accurate and reliable. This processed data includes indices for VOCs and NOx and precise measurements for PM, RH, and T.

#### Communication
The ESP32 uses the ESP-NOW protocol, which allows direct, peer-to-peer communication between ESP32 devices. This protocol is efficient and low-latency, eliminating the need for a central server. Each device has a unique MAC address, enabling them to send and receive data directly from one another.

#### Data Transmission
Processed data is transmitted from the ESP32 to a Supabase database via Wi-Fi. Supabase is the central repository for all collected data, enabling remote access and real-time monitoring through the ITUS web dashboard.

#### Web Dashboard
The ITUS web dashboard, built using Streamlit, allows users to visualize and analyze the data collected by the ITUS Blue prototype. It provides interactive charts for PM levels, VOC levels, humidity, and temperature, along with a map showing the device's location.

![Screenshot 2024-05-27 120310](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/6748ec91-12ab-46bd-bb2f-c96892f3bc51)
![Screenshot 2024-05-27 120230](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/3c7c97eb-58d7-427e-8931-e0c6606fd449)
![Screenshot 2024-05-27 120206](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/0dccbb7a-a6fd-472d-b233-2b6470f73098)
![Screenshot 2024-05-27 120142](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/a61f5a6d-7a53-46eb-bdf9-af0380110720)
![Screenshot 2024-05-27 120049](https://github.com/AryanKumarNadipally/ITUS/assets/143588978/39c59d09-721d-465a-ba21-8c54a5face19)


### Power Consumption
The daily cost of running the ITUS device is approximately $0.001871 at commercial rates (11.5 ¢/kWh) and $0.002353 at residential rates (14.46 ¢/kWh). The ESP32 consumes an average of 160 mA at 3.3V, resulting in 0.528W of power. The SEN55 sensor consumes 30 mA at 5V, equating to 0.15W. Together, the total power consumption is 0.678W. Over 24 hours, this translates to 16.272 Wh or 0.016272 kWh, making the ITUS device highly energy-efficient.

### Cost of Building the Prototype
- **ESP32:** $6
- **SEN55:** $35
- **12V Power Supply:** $10
- **3D Printed Filament:** $10
- **UV Coating:** $12
- **Total Cost:** $72

## Future Work
### Scalability
- **Integrating Multiple Devices:** Deploy numerous ITUS devices across urban areas to form a comprehensive environmental monitoring network. Each device will communicate via ESP-NOW, creating a robust, decentralized system that enhances data reliability and coverage.

### Advanced Web Dashboard
- **Enhanced Data Visualization:** Improve the dashboard with interactive features, heat maps, and predictive analytics tools.
- **User Customization:** Allow users to customize their data views and receive notifications for specific environmental thresholds.

### Machine Learning
#### Algorithms
- **Time Series Analysis:** Use ARIMA (AutoRegressive Integrated Moving Average) to predict future environmental conditions based on historical data.
- **Classification Models:** Implement decision trees or random forests to classify air quality levels and identify patterns.
- **Regression Models:** Utilize linear regression or neural networks to correlate environmental factors with UHI intensity.
- **Clustering:** Apply k-means clustering to segment data into distinct groups for detailed analysis.

#### Applications
- **Predictive Maintenance:** Forecast sensor maintenance needs to ensure continuous data collection.
- **Anomaly Detection:** Identify unusual environmental patterns or sudden changes in air quality.
- **Impact Assessment:** Evaluate the effectiveness of urban planning measures on UHI reduction.

By integrating these advanced algorithms and expanding the ITUS network, we aim to provide deeper insights into the Urban Heat Island effect and develop more effective mitigation strategies.

## Acknowledgments
I extend my deepest gratitude to several individuals and institutions who have significantly contributed to the development and success of the ITUS project.

### Professor Michelle Fehler
Michelle Fehler, my instructor for this course, has profoundly influenced this project. As a Clinical Associate Professor at The Design School and an Affiliated Faculty at the Center for Biodiversity Outcomes, her expertise in biomimicry and life-centered design thinking guided me through the conceptualization and development phases. Her continuous support, suggestions, and encouragement were invaluable.

### Professor Darren Petrucci
Darren Petrucci, the Suncor Professor at The Design School and a Senior Sustainability Scientist at the Global Institute of Sustainability, played a crucial role in shaping the project's design. His extensive knowledge of design thinking and urban infrastructure ensured a user-centric solution for the ITUS project.

### Professor Sangram Redkar
Dr. Sangram Redkar, Associate Director and Professor at the School of Manufacturing Systems and Networks, provided crucial support and guidance. As my committee chair, Dr. Redkar facilitated my course registration for RAS 590. I am always thankful to Professor Redkar.

### Advisor Sami Taddio
I sincerely thank my advisor, Sami Taddio, for her unwavering support and guidance throughout the course registration process. Sami helped me navigate the enrollment for courses not conventionally listed in my elective options, ensuring I could integrate these vital interdisciplinary courses into my curriculum.

### School of Manufacturing Systems and Networks & Herberger Institute for Design and the Arts
I am grateful to these departments for offering interdisciplinary courses like RAS 590 and ARC 602. These courses provided a platform for hands-on learning with GEN AI tools, UX/UI tools, 3D modeling, and archetype tools. The collaborative environment fostered by Professors Fowler and Darren allowed me to approach problem-solving with a design-thinking mindset, significantly enhancing the project's practical impact.

### Arizona State University (ASU) Graduate & Professional Student Association (GPSA)
I express my gratitude for the GPSA Jumpstart Research Grant, which provided $750 in funding for this project. This financial support was essential in procuring the necessary materials and components for the ITUS prototype.
