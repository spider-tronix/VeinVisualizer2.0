# Vein Visualizer 1.0

The project **Vein Visualizer** was started as an idea for **Sangam 2019**. The concept of the project is to make the **Intravenous Injection** procedure a hassle free one. Injecting takes lots of expertise and skill to do. Firstly, finding the proper spot is not an easy task. And adding to this, there are lots of other parameters that affect the visibility of the veins. 

We used Near Infrared Imaging techniques to enhance the visibility of the veins. A prototype was made and proof of the concept is verified. 

### Input frame
![Input frame](https://github.com/spider-tronix/VeinVisualizer2.0/blob/master/1.png)
### Contrast adjustment frame
![Contrast adjustment frame](https://github.com/spider-tronix/VeinVisualizer2.0/blob/master/1clahe.png)
### Masked Output
![Masked Output](https://github.com/spider-tronix/VeinVisualizer2.0/blob/master/1mask.png)


# Vein Visualizer 2.0

With the creation of prototype being successful, the process of developing and improving it comes next. Based on the suggestions given by the visitors of our Sangam stall, the project takes a new face. The new concept is to make the device movable and more flexible to use. Moreover the idea/device should be accessible easily and friendly to use. 

So, we are moving towards **Smartphone** based solution, which will be able to  capture, process and display the NIR live feed. With **real time processing** being the priority, improvement in algorithms should be done as well.

## App development
Since the project needs app development to be done, we are looking forward to take in people who are good at **Android** development and willing to work with **OpenCV** binders for Java.   The app developer will get a good insight on image processing techniques.
Source code for the app can be found here: https://github.com/gouthamcm/Vien_Visualizer

# Process Flow
We shall be ideating on new features which are shall be possible with the android device. Optimizations will be taken care by the image processing team members, while the implementation of the optimizations in java/OpenCV binders will be done by the app developer.
The process will be continued till the app reaches final stage of maturity.

## TODO:
### Code/Software:

-  [x] Camera calibration for images.
-  [x] Parameter variations and tuning.
-  [x] Finding k1, k2, k3 for specific screen.
-  [ ] Optimizing Image Processing algorithm for better visuals.
-  [x] Merging modules together.
-  [ ] Threading and further optimizations.
  
### Hardware:
-  [x] Get the VR headset
-  [x] Get the Screen 
-  [x] Running Codes in RPi + Camera and benchmarking
-  [ ] Adding driver/dependancies for Screen
-  [ ] IR LED lighting setup
-  [ ] 3D casing enclosure.
