# Photo Reader GUI

![image](https://github.com/ilx23/Photo-Reader-GUI/assets/91822811/4e209140-7046-4375-9a54-954dfd7268fd)

## Introduction:

Welcome to the Photo Reader GUI project! This project provides a simple Graphical User Interface (GUI) for reading and displaying text from images. Users can easily extract text from photos and view the results directly within the application.

## Features:

1. **User-Friendly Interface:** The GUI offers an intuitive interface for users to select images and extract text effortlessly.

2. **Text Extraction:** Using optical character recognition (OCR) technology, the application extracts text from images and displays it to the user.

3. **Image Support:** The application supports a wide range of image formats, allowing users to process photos captured from various devices.

## How to Use:

1. **Clone the Repository:** Clone this repository to your local machine using the following command:
> ```git clone https://github.com/ilx23/Photo-Reader-GUI.git```

2. **Install Dependencies:** Ensure you have Python installed on your machine. Additionally, you need to have the Tesseract OCR engine and the pytesseract library installed. You can install pytesseract using pip:
> ```pip install pytesseract```

3. **Download Tesseract:** Download and install the Tesseract OCR engine from the official [GitHub repository](https://github.com/tesseract-ocr/tesseract).

4. **Set Tesseract Path:** After installing Tesseract, set the Tesseract executable path in the code (line 17) to the location where Tesseract is installed on your system.

5. **Run the Application:** Navigate to the project directory and run the following command:
> ```python app.py```

6. **Select Image:** Click on the "Select Image" button to choose the image file from which you want to extract text.

7. **Read Text:** Once the image is selected, click on the "Read Text" button to extract and display the text from the image.

## Contributing:

Contributions to this project are welcome! If you have any suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments:

This project was inspired by the need for a simple tool to extract text from images with a graphical interface. Special thanks to the developers of Tkinter and pytesseract for providing easy-to-use libraries for GUI development and text extraction, respectively.

## Contact:

For any inquiries or support, feel free to contact the project maintainer [here](mailto:iliakeshavarz23@gmail.com).

**Effortlessly extract text from images with the Photo Reader GUI!**
