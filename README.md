# IUCN Species Scraper  

## Overview  
This project is a **Selenium-based web scraper** that extracts species data from the **IUCN Red List** and saves it into a structured CSV file.  
The **International Union for Conservation of Nature (IUCN)** maintains the Red List, a comprehensive source of information on the **global conservation status** of animal, fungi, and plant species.  
This scraper automates the process of collecting species information for further analysis and research.  

---

## Features  

- **Automated Web Scraping** – Extracts species data directly from the **IUCN Red List website**.  
- **Data Storage** – Saves scraped data into a structured **CSV file** (`data/species_data.csv`).  
- **Headless Browsing** – Supports **headless mode** (running the scraper without opening a browser window).  
- **Cross-Platform Compatibility** – Works on **Windows, macOS, and Linux** using `webdriver-manager`.  
- **Easy Setup** – Requires minimal configuration using `requirements.txt`.  

---

## Installation & Setup  

### Step 1: Clone the Repository  
To get started, first clone this repository to your local machine:  
```sh
git clone https://github.com/yourusername/selenium-iucn-scraper.git
cd selenium-iucn-scraper
