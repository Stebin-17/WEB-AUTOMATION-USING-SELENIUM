<h1 align ='center'> WEB-AUTOMATION-USING-SELENIUM </h1>

<h2>INTRODUCTION</h2>


Web automation has become increasingly important in today's fast-paced digital world, enabling businesses and developers to streamline repetitive tasks, perform complex data extraction, and improve overall efficiency. The project "Web Automation using Selenium" aims to leverage the power of Selenium, a widely-used open-source web testing framework, to automate various web-related tasks and interactions.

Selenium allows users to write test scripts in multiple programming languages, such as Python, Java, C#, and Ruby, and supports popular web browsers like Chrome, Firefox, Safari, and Edge. By using Selenium WebDriver, an API that allows users to control browser actions programmatically, this project will simulate user interactions with websites and automate tasks such as form filling, web scraping, and navigation.The project will focus on creating reusable automation scripts for a diverse range of web applications, ensuring that the developed solution is adaptable to various use cases. This web automation system will not only save time and effort but also reduce the likelihood of human errors in routine tasks, leading to increased productivity and enhanced data accuracy.

<p align="center">
  <img src="https://user-images.githubusercontent.com/114398468/232456792-4c31322d-2ddb-4882-9e3a-598dd5911b7d.png" width ="50%"/>
</p>

#

<h2> CODE EXPLANATION </h2>

> email_generator.py

This Python script is designed to generate a list of random, authenticated email addresses and write them to a CSV file. The script uses the faker library to generate random names and the email_validator library to validate email addresses. Here's an explanation of each function in the script:

- ```generate_email()```: This function generates a random email address by creating a random first name, last name, and selecting a domain from a predefined list. It then combines these elements to form an email address.

- ```generate_authenticated_emails(num_emails)```: This function generates a list of authenticated email addresses by calling the generate_email() function num_emails times. It then validates the generated email address using the email_validator library. If the email is valid, it's added to the list of emails; otherwise, it's ignored. Finally, the function removes duplicates from the list of emails and returns the list.

- ```write_emails_to_csv(filename, emails)```: This function writes the list of email addresses to a CSV file with the specified filename. It opens the file in write mode and iterates over the list of emails, writing each email address as a new row in the CSV file.

To use this script, you would need to call the generate_authenticated_emails() function with the desired number of email addresses and then pass the resulting list to the write_emails_to_csv() function along with the desired output filename. For example:

```
num_emails = 100
output_filename = "emails.csv"

emails = generate_authenticated_emails(num_emails)
write_emails_to_csv(output_filename, emails)
```
This example would generate 100 random, authenticated email addresses and write them to a file named "emails.csv".

> selenium_loop.py

This Python script generates random, authenticated email addresses and uses them to fill out a form on a specified web page. It utilizes the Selenium WebDriver for automating web browser interactions and the custom email generator script email_generator to generate emails.

Here's an explanation of each part of the script:

- Import necessary libraries: The script imports the required libraries and modules, such as ```Selenium WebDriver```, ```WebDriverWait```, ```expected_conditions```, ```ChromeOptions```, and the custom email generator script.

- Generate email addresses: The script generates 3000 random, authenticated email addresses using the ```generate_authenticated_emails()``` function from the email_generator script and writes them to a CSV file.

- Read email addresses from the CSV file: The script reads the email addresses from the CSV file and stores them in the emails list.

- Set up the browser: The script initializes a Chrome WebDriver instance with pop-up blocking options to disable notifications and pop-ups.

- Navigate to the web page: The script navigates to the specified web page and maximizes the browser window.

- Iterate through the email addresses: The script loops through each email address in the emails list and performs the following actions:

      a. Enter the email address in the email input field.
      b. Click the checkbox on the form.
      c. Click the submit button on the form.
      d. Stop the page loading once the form is submitted.

If an exception occurs during the process, the script logs the error message using the logging module.

To use this script, replace "web-address" with the URL of the target web page and update the By.ID and By.XPATH locators as needed to match the input field, checkbox, and submit button on the page.

This script is useful for automating form submissions on web pages, particularly when dealing with a large number of email addresses or when testing the functionality of an email subscription form.

#

<h2> CONCLUSION </h2>

The Web Automation Using Selenium project has demonstrated the effective application of Selenium WebDriver for automating form submissions and browser interactions on web pages. By incorporating a custom email generator script and leveraging the powerful capabilities of Selenium, the project successfully automated the process of filling out and submitting a form using a large number of randomly generated, authenticated email addresses.

The project not only saved time and effort compared to manual form submissions but also showcased the adaptability of Selenium WebDriver for various web automation tasks. Furthermore, the script accounted for real-world challenges such as handling pop-ups and notifications, ensuring a smooth user experience.This project serves as a foundation for future web automation endeavors, where Selenium can be used to automate a wide range of tasks, from web scraping and data extraction to automated testing and performance monitoring. By expanding upon the concepts and techniques demonstrated in this project, developers and businesses can further streamline their workflows, enhance productivity, and ensure the accuracy and reliability of web-based operations.

#

