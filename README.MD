# Mortgage Calculator

## Overview

The **Mortgage Calculator** is a Django-based web application designed to calculate mortgage details based on user input. It allows users to enter loan amount, loan term, and interest rate to calculate monthly payments, total payment, and total interest. The application features a user-friendly interface with a responsive design.

## Features

- **Input Fields:**
  - Loan Amount (EUR)
  - Loan Term (Years)
  - Interest Rate (%)

- **Results Display:**
  - Monthly Payment
  - Total Payment
  - Total Interest
  - Loan Details

- **Additional Functionality:**
  - **Calculate Button:** Computes the mortgage details.
  - **Clear Button:** Resets the input fields and hides the results.
  - **Styling:** Modern design with Bootstrap and custom CSS.
  - **Icons:** Font Awesome icons for improved UI.
  - **Animations:** Smooth hover effect on buttons.
  - **Background Image:** A visually appealing background image.

## Technologies Used

- **Backend:** Django (Python)
- **Frontend:**
  - HTML
  - CSS (custom styles and Bootstrap 5)
  - JavaScript (clear button functionality)
  - Font Awesome (for icons)
- **Static File Serving:** WhiteNoise

## Folder Structure

```
Mortgage_calculator/
|
|-- calculator/
|   |-- migrations/
|   |-- static/
|   |   |-- css/
|   |   |   |-- styles.css
|   |   |-- img/
|   |   |   |-- 1.jpg
|   |   |-- js/
|   |       |-- scripts.js
|   |-- templates/
|       |-- calculator/
|           |-- mortgage_calculator.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|
|-- manage.py
```

## Setup and Installation

1. **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd Mortgage_calculator
    ```

2. **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**
    ```bash
    python3 manage.py migrate
    ```

5. **Run the Development Server:**
    ```bash
    python3 manage.py runserver
    ```

6. **Access the Application:**
    Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

7. **Deployed Application:**
    Access the deployed application at [https://mortgage-calculator-9gw8.onrender.com](https://mortgage-calculator-9gw8.onrender.com).

## How to Use

1. Enter the loan amount, loan term (in years), and interest rate (%).
2. Click the **Calculate** button to see the results.
3. To clear the form and hide the results, click the **Clear** button.

## Future Enhancements

- Add support for multiple currencies.
- Include additional loan types (e.g., fixed, adjustable).
- Add a database feature to save calculations for registered users.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- **Django Framework** for providing a robust backend solution.
- **Bootstrap 5** for responsive design.
- **Font Awesome** for elegant icons.
- **Community Resources** for tutorials and guidance.

