import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
wait = WebDriverWait(driver, 15)

# Base URL template
base_url_template = "http://rtmc.emploi.nat.tn/dm/index.php/rtmcdp/listedp/{}"

# Final combined output file
final_output_file = "all_jobs_data_combined.json"
all_jobs_data_combined = []  # List to store all combined data

# Iterate through the range of letters A to N
for letter in range(ord('A'), ord('N') + 1):
    current_letter = chr(letter)
    main_page_url = base_url_template.format(current_letter)
    output_file = f"all_jobs_data_{current_letter}.json"  # File for the current letter
    all_jobs_data = []  # List to store all jobs data for the current letter

    # Open the main page for the current letter
    driver.get(main_page_url)
    time.sleep(3)  # Let the page load

    while True:
        # Get all job links on the main page
        job_links = driver.find_elements(By.CSS_SELECTOR, ".table a")  # Adjust selector as needed

        for i in range(len(job_links)):
            try:
                # Re-fetch job links to avoid stale references
                job_links = driver.find_elements(By.CSS_SELECTOR, ".table a")
                job_link = job_links[i]
                job_url = job_link.get_attribute("href")

                print(f"Scraping job from {job_url}")

                # Open the job detail page
                driver.get(job_url)
                time.sleep(3)

                # Extract job name directly from the page
                try:
                    job_name = driver.find_element(By.CSS_SELECTOR, "h4").text.strip()  # Adjust CSS selector for job name
                    print(f"Scraped job name: {job_name}")
                except Exception as e:
                    job_name = "Unknown Job"
                    print(f"Error extracting job name: {e}")

                # Prepare data structure
                job_data = {
                    "job_name": job_name,
                    "appellations": None,
                    "identité": None,
                    "compétences": None,
                }

                try:
                    # Scrape APPELLATIONS
                    appellations_tab = wait.until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#appellations']"))
                    )
                    appellations_tab.click()
                    time.sleep(1)
                    appellations_content = driver.find_element(By.CSS_SELECTOR, "#appellations .table-responsive-sm").text
                    job_data["appellations"] = appellations_content
                    print(f"Scraped APPELLATIONS for {job_name}")

                    # Scrape IDENTITÉ
                    identité_tab = driver.find_element(By.CSS_SELECTOR, "a[href='#identite']")
                    identité_tab.click()
                    time.sleep(1)
                    identité_content = driver.find_element(By.CSS_SELECTOR, "#identite .accordion").text
                    job_data["identité"] = identité_content
                    print(f"Scraped IDENTITÉ for {job_name}")

                    # Scrape COMPÉTENCES
                    compétences_tab = driver.find_element(By.CSS_SELECTOR, "a[href='#competences']")
                    compétences_tab.click()
                    time.sleep(1)
                    compétences_content = driver.find_element(By.CSS_SELECTOR, "#competences .accordion").text
                    job_data["compétences"] = compétences_content
                    print(f"Scraped COMPÉTENCES for {job_name}")

                except Exception as e:
                    print(f"Could not scrape all sections for {job_name}: {e}")

                # Append the job data to the list
                all_jobs_data.append(job_data)
                print(f"Added {job_name} data to the list")

            except Exception as e:
                print(f"Error processing job link: {e}")
            
            # Return to the main page
            driver.get(main_page_url)
            time.sleep(2)

        break

    # Save all jobs data for the current letter to a JSON file
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(all_jobs_data, json_file, ensure_ascii=False, indent=4)

    print(f"Scraping completed for letter {current_letter}. Data saved in {output_file}")

    # Add the data to the combined list
    all_jobs_data_combined.extend(all_jobs_data)

# Save the combined data to a single JSON file
with open(final_output_file, "w", encoding="utf-8") as json_file:
    json.dump(all_jobs_data_combined, json_file, ensure_ascii=False, indent=4)

print(f"All jobs data combined and saved in {final_output_file}")

# Close the driver
driver.quit()
