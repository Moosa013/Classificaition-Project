# News Article Classification Project
This project uses a variety of libraries for data manipulation, visualization, machine learning, and model deployment. Follow the instructions below to recreate the environment and run the project.
____

# Project Setup
### 1. Clone the Repository

git clone https://github.com/Moosa013/Classification-Project.git

___
### 2. Create a Virtual Environment
We recommend using a virtual environment to isolate the dependencies for this project. There are many ways to do this, we've outlined one such method below.

#### 2.1 Create the new evironment - you only need to do this once

```bash
# create the conda environment
conda create --name <env>
```

#### 2.2 Activate the new evironment 

Once you have created the new environment, you then need to activate it and then install the pip package. This pip package will enable you to install the dependent packages that this environment needs in order to run the project. The list of dependencies is outlined in the requirements.txt file - available in the GitHub Repo.

```bash
# activate the virtual environment
conda activate <env>
# install the pip package
conda install pip
```

___
### 3. Install Dependencies
Install the required dependencies using the requirements.txt file. Run the following command inside your virtual environment:

```bash
# install the requirements for this project
pip install -r requirements.txt
```

### 4. Running the App
After setting up the environment on your local machine, you can run the project using the Streamlit app or directly in a Jupyter notebook. Here's how to run the Streamlit app. The below command should be run within a Git bash (Windows), or terminal (Mac/Linux):

```bash
# running the streamlit app.py file saved from the notebook
streamlit run app.py
```

For running the project scripts or Jupyter notebooks, simply execute the desired script or open the notebook and run the cells.

___ 

# Project Requirements
The following Python packages are required for this project:

## Packages
* **pandas**: Data manipulation and analysis library, providing data structures like DataFrames.
* **numpy**: Essential package for numerical computing and array manipulation.
* **matplotlib**: Plotting library for creating static, interactive, and animated visualizations.
* **seaborn**: Statistical data visualization based on matplotlib, providing easier interface and beautiful plots.
* **nltk**: Natural Language Toolkit for processing and analyzing human language data (text).
* **sklearn**: Scikit-learn, a machine learning library for building models and performing tasks like classification, regression, and clustering.
* **imblearn**: Library to handle imbalanced datasets, providing methods like SMOTE for oversampling.
* **wordcloud**: Generates word clouds from text data to visualize the most frequent words.
* **xgboost**: Gradient boosting framework for high-performance, scalable machine learning.
* **streamlit**: Framework for building interactive, web-based data applications.
* **joblib**: Efficient serialization of Python objects, used for saving and loading models.
* **warnings**: Provides a mechanism to manage warnings in Python, commonly used to suppress warnings in scripts.
