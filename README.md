
# Gender Prediction Model

This project is a machine learning model designed to predict a person's gender based solely on their first name. Developed during my third year of undergraduate studies, it served as a practical application of the machine learning concepts I was learning at the time.

## Project Overview

The Gender Prediction Model utilizes a Naive Bayes classifier to infer gender from first names. It is implemented in Python, with a web interface built using the Flask framework. The model is trained on a dataset of names and their associated genders, enabling it to make predictions on new, unseen names.

## Features

- **Machine Learning Model**: Employs a Naive Bayes classifier for gender prediction.
- **Web Interface**: Provides an interactive user interface built with Flask.
- **Data Handling**: Includes scripts for loading and processing name data.

## Installation and Setup

To run this project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/abhinavsaurabh/genderprediction.git
   cd genderprediction
   ```

2. **Set Up a Virtual Environment**:

   Ensure you have `virtualenv` installed. If not, install it using `pip`:

   ```bash
   pip install virtualenv
   ```

   Create and activate the virtual environment:

   ```bash
   virtualenv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:

   Start the Flask development server:

   ```bash
   python app.py
   ```

   Access the application by navigating to `http://localhost:5000` in your web browser.

## Usage

Enter a first name into the input field on the web interface, and the model will predict and display the likely gender associated with that name.

## Project Structure

- `app.py`: Main Flask application file that runs the web server.
- `gender_predictor.py`: Contains the implementation of the Naive Bayes classifier for gender prediction.
- `USSSALoader.py`: Script for loading and processing the dataset of names and genders.
- `templates/`: Directory containing HTML templates for the web interface.
- `static/`: Directory for static files such as CSS and JavaScript.

## Dataset

The model is trained on a dataset comprising first names and their corresponding genders. The dataset is included in the repository under the `gender-data/` directory.

## Future Enhancements

- **Model Improvement**: Explore more advanced machine learning algorithms to enhance prediction accuracy.
- **Expanded Dataset**: Incorporate a more diverse and comprehensive dataset to improve model generalization.
- **Deployment**: Deploy the application to a cloud platform for broader accessibility.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

This project was developed as part of my journey into machine learning during my undergraduate studies. Special thanks to the open-source community for providing valuable resources and inspiration.

---

*Note: This project was created as a learning exercise during my third year of undergraduate studies in machine learning.*
