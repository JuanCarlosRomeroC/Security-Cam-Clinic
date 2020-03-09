# Object-Triggered Cam for Women Safety
YoloV3 / tiny-YoloV3 + RaspberryPi4 / Ubuntu LaptopPC + NCS/NCS2 + USB Camera + Python
  
Inspired from **https://github.com/PINTO0309/OpenVINO-YoloV3**

# Project Idea

The project is a tribute to women safety on the day of International Women's day. 

**The person can show an object to the cam and it would trigger a sequence of events. The YOLO Module can detect trained COCO objects. Once a particular object, say a cell phone, is detected then the Raspberry Pi system would publish a message to MQTT brocker via Alert Channel. When the message is received by the MQTT Client then it would trigger an SMS and Phone call (to police station or relatives) via Twilio integration.** 

The clip of the event can be sent over FFMpeg and sent as an MMS. Going  forward, the Yolo or Tiny Yolo can be re-trained with custom objects to trigger the chain of events.

## To Execute:

YoloV3
$ python3 openvino_yolov3_test.py
tiny-YoloV3 + NCS2 MultiStick
$ python3 openvino_tiny-yolov3_MultiStick_test.py -numncs 1
YoloV3 + NCS2 MultiStick (Pretty slow)
$ python3 openvino_yolov3_MultiStick_test.py -numncs 4

![Cam in Action]{IMG_1318.jpg}
