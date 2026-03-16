Network Traffic Analyzer
This project is a simple network traffic analyzer that captures network packets and counts the number of packets for different protocol types, including TCP, UDP, and ICMP. It provides statistics on the captured packets once the capture is stopped.

Features
Captures network packets in real-time.
Identifies and counts packets by protocol type (TCP, UDP, ICMP).
Displays packet statistics after the capture is stopped.
Installation
To run this project, you need to have Python installed on your system. You also need to install the required dependencies listed in requirements.txt.

Clone the repository:

git clone <repository-url>
cd network-traffic-analyzer
Install the required packages:

pip install -r requirements.txt
Usage
Run the application:

python main.py
The application will start capturing packets. Press Ctrl+C to stop the capture.

After stopping the capture, the application will display the statistics of the captured packets.

License
This project is licensed under the MIT License.
