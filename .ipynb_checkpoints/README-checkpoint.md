# News Article Classification Project
This project uses a variety of libraries for data manipulation, visualization, machine learning, and model deployment. Follow the instructions below to recreate the environment and run the project.
____

# Project Setup
### 1. Clone the Repository

git clone https://github.com/Tiisetso-G/NLP-Group-Project.git

### 2. Create a Virtual Environment
We recommend using a virtual environment to isolate the dependencies for this project.

Option 1: Using venv

python -m venv venv

Option 2: On Windwos or MacOS/Linux
* Windows:
  
  .\venv\Scripts\activate

* MacOS/Linux

  source venv/bin/activate

### 3. Install Dependencies
Install the required dependencies using the requirements.txt file. Run the following command inside your virtual environment:

pip install -r requirements.txt

### 4. Running the Project
After setting up the environment, you can run the project using Streamlit or directly in a Jupyter notebook. Here's how to run the Streamlit app:

streamlit run app.py

For running the project scripts or Jupyter notebooks, simply execute the desired script or open the notebook and run the cells.

___ 

# Project Requirements
The following Python packages are required for this project:

## Packages
pandas: Data manipulation and analysis library, providing data structures like DataFrames.
numpy: Essential package for numerical computing and array manipulation.
matplotlib: Plotting library for creating static, interactive, and animated visualizations.
seaborn: Statistical data visualization based on matplotlib, providing easier interface and beautiful plots.
nltk: Natural Language Toolkit for processing and analyzing human language data (text).
sklearn: Scikit-learn, a machine learning library for building models and performing tasks like classification, regression, and clustering.
imblearn: Library to handle imbalanced datasets, providing methods like SMOTE for oversampling.
wordcloud: Generates word clouds from text data to visualize the most frequent words.
xgboost: Gradient boosting framework for high-performance, scalable machine learning.
streamlit: Framework for building interactive, web-based data applications.
joblib: Efficient serialization of Python objects, used for saving and loading models.
warnings: Provides a mechanism to manage warnings in Python, commonly used to suppress warnings in scripts.
