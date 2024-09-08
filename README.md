# Meme Explainer Bot

## Overview

The **Meme Explainer Bot** is a fun and interactive application that uses artificial intelligence to explain memes and their context. This bot leverages natural language processing and image recognition to analyze memes and provide insightful descriptions and background information.

## Features

- **Image Analysis**: Recognizes and classifies meme templates.
- **Contextual Explanation**: Provides detailed explanations of meme content and its cultural significance.
- **User Interaction**: Allows users to upload memes and receive explanations in real-time.

## Technologies Used

- **Python**: Programming language for building the bot.
- **TensorFlow/Keras**: For image recognition and deep learning models.
- **Flask**: For creating the web service.
- **OpenAI GPT**: For generating explanations and handling natural language tasks.
- **Pillow**: For image processing.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/koushik2k3/Meme-Explainer-Bot
    cd meme-explainer-bot
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    conda create --name tf python=3.9
    conda activate tf
    ```
3. GPU setup
   
You can skip this section if you only run TensorFlow on CPU.

    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```
    
4. Install Tensorflow (Caution: TensorFlow 2.10 was the last TensorFlow release that supported GPU on native-Windows. Starting with TensorFlow 2.11, you will need to install TensorFlow in WSL2, or install tensorflow-cpu and, optionally, try the TensorFlow-DirectML-Plugin)
   
        ```bash
        pip install "tensorflow<2.11"
        ```

5. Verify installation
   
    Verify the CPU setup:
       ```bash
    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
        ```
   If a tensor is returned, you've installed TensorFlow successfully.

   Verify the GPU setup:
        ```bash
        python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))" 
        ```
    If a list of GPU devices is returned, you've installed TensorFlow successfully.
 
6. Install the required packages using the requirements.txt file:


7. Set up the environment variables (e.g., OPEN AI API keys, model paths) in a `.env` file or directly in your environment.

## Usage

1. Start the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and go to `http://localhost:5000` to interact with the bot.

3. Upload a meme image and get an explanation!

## Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Flask](https://flask.palletsprojects.com/)
- [OpenAI](https://www.openai.com/)

