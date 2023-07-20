<!DOCTYPE html>
<html>
<head>
  <title>Face Recognition Attendance System</title>
</head>
<body>
  <h1>Face Recognition Attendance System</h1>
  <img src="face_recog.png" alt="Face Recognition Attendance System">

  <p>This repository contains a Face Recognition Attendance System developed using Python and the OpenCV library for face detection and recognition. The system enables automatic attendance recording based on facial recognition of individuals.</p>

  <h2>Features</h2>
  <ul>
    <li>Utilizes the OpenCV library for face detection and recognition.</li>
    <li>Implements the K-nearest neighbors (KNN) algorithm for face recognition.</li>
    <li>Saves the faces of individuals in a dataset for training the model.</li>
    <li>Automatically records attendance and timestamps when recognized faces are detected.</li>
    <li>Uses Streamlit to provide a user-friendly web interface for monitoring attendance.</li>
  </ul>

  <h2>Installation</h2>
  <ol>
    <li>Clone the repository:
      <pre><code>git clone [https://github.com/bugbreaker18/Machine_Learning.git](https://github.com/bugbreaker18/Machine_Learning.git)</code></pre>
    </li>
    <li>Install the required dependencies:
      <pre><code>pip install opencv-python pyttsx3 pandas streamlit streamlit_autorefresh</code></pre>
    </li>
  </ol>

  <h2>Usage</h2>
  <ol>
    <li>Execute the <code>add_faces.py</code> script to collect face data for attendance.
      <pre><code>python add_faces.py</code></pre>
    </li>
    <li>The script will prompt you to enter your name and then start capturing your face for training the model.</li>
    <li>The script will capture your face images and store them in the <code>data/faces_data.pkl</code> file, along with the corresponding names in <code>data/names.pkl</code>.</li>
    <li>Execute the <code>test.py</code> script to enable the face recognition attendance system.
      <pre><code>python test.py</code></pre>
    </li>
    <li>The script will activate the webcam and start recognizing faces. When a recognized face is detected, it will record the attendance in the CSV file located in the <code>Attendance</code> folder.</li>
    <li>Execute the <code>app.py</code> script to visualize the attendance records using a Streamlit web interface.
      <pre><code>streamlit run app.py</code></pre>
    </li>
  </ol>

  <h2>How It Works</h2>
  <p>The Face Recognition Attendance System works in the following steps:</p>
  <ol>
    <li>The <code>add_faces.py</code> script captures face images of individuals, resizes them, and stores them in the dataset.</li>
    <li>The face data, along with the corresponding names, is saved in <code>data/faces_data.pkl</code> and <code>data/names.pkl</code>.</li>
    <li>The <code>test.py</code> script uses the KNN algorithm to train a model with the collected face data.</li>
    <li>When the <code>test.py</code> script is executed, the webcam is activated to detect and recognize faces in real-time.</li>
    <li>Recognized faces are marked with their names and attendance is recorded in CSV files located in the <code>Attendance</code> folder, including timestamps.</li>
    <li>The <code>app.py</code> script provides a user-friendly web interface to view attendance records using Streamlit.</li>
  </ol>

  <h2>What It Lacks</h2>
  <p>The Face Recognition Attendance System has several limitations and areas for improvement:</p>
  <ul>
    <li>Currently, the system relies on a simple K-nearest neighbors (KNN) algorithm for face recognition, which may not be as accurate as more advanced deep learning-based models.</li>
    <li>The dataset used for training the model is relatively small (limited to 100 faces), which may affect the model's performance and generalization.</li>
    <li>There might be issues with face recognition under varying lighting conditions, angles, and facial expressions.</li>
    <li>The system may not handle large-scale attendance recording efficiently and may require optimization for performance.</li>
    <li>It lacks a user authentication mechanism, making it vulnerable to unauthorized attendance marking.</li>
  </ul>

  <h2>Contributing</h2>
  <p>Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.</p>



  <h2>Acknowledgments</h2>
  <ul>
    <li>The Face Recognition Attendance System utilizes the OpenCV library for face detection and recognition.</li>
    <li>The K-nearest neighbors (KNN) algorithm from scikit-learn is used for face recognition.</li>
    <li>The Streamlit library is used for creating a user-friendly web interface to view attendance records.</li>
  </ul>
  <p>Special thanks to the Python community and the developers of the libraries used in this project for their valuable contributions.</p>
</body>
</html>
