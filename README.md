# Meme Explainer Bot

## Overview

The **Meme Explainer Bot** is a fun and interactive application that uses artificial intelligence to explain memes and their context. This bot leverages natural language processing and image recognition to analyze memes and provide insightful descriptions and background information. Currently trained on templates - {Arthur's fist, Surprised Pikachu, It's free real estate, This is fine dog, Distracted Boyfriend and Flex Tape}

![Output](https://github.com/user-attachments/assets/789c3da3-e217-47ff-9184-d413dc2648fa)

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
    git clone https://github.com/koushik2k3/Meme-Explainer-Bot.git
    cd Meme-Explainer-Bot
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    conda create --name tf python=3.9
    conda activate tf
    ```

3. GPU setup (skip if you only use TensorFlow on CPU):

    ```bash
    conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
    ```

4. Install TensorFlow (Caution: TensorFlow 2.10 was the last release that supported GPU on native Windows. For TensorFlow 2.11 and later, use WSL2 or install TensorFlow-CPU and optionally try TensorFlow-DirectML-Plugin):

    ```bash
    pip install "tensorflow<2.11"
    ```

5. Verify installation:

    Verify the CPU setup:

    ```bash
    python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
    ```

    If a tensor is returned, TensorFlow is installed successfully.

    Verify the GPU setup:

    ```bash
    python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
    ```

    If a list of GPU devices is returned, TensorFlow is configured correctly for GPU.

6. Install the required packages using the `requirements.txt` file:

7. Set up the environment variables (e.g., OpenAI API keys, model paths) in a `.env` file or directly in your environment.

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
