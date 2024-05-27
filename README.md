# Final-Project
### Project Description

This project has been designed and developed for the purpose of teaching and applying electrical engineering concepts. It provides the necessary calculations using the Python programming language. This project is single-authored and presented in person. The total score for this project is 2 marks.

**Note:** Data should be stored in files, and user inputs and outputs should be saved and displayed upon request. Users should have the ability to modify or delete saved inputs and outputs. Proper and appropriate commenting is required. Necessary functions should be defined, and appropriate comments should be provided for each code.

### Question 1 – Hogwarts Phone Line

At Hogwarts University, to facilitate communication between students and their respective group professors, they intend to set up a telephone system. Unfortunately, only one phone line is allocated for the Snape and Gryffindor offices. University officials have asked for your assistance to write a program that receives data sent to this line as input and delivers relevant data for the Snape and Gryffindor offices separately as output.

The only difference between the data sent to these two offices is the frequency of the transmission. The signal you receive is the sum of these two signals.

#### Frequency ?? What is it anyway ??

![Alt text](https://github.com/CP-NIT/Final-Project/blob/main/s1_1.png)

Well, in a very simple sense, we can say the frequency of a signal is higher when it has more sudden changes. For example, let's consider two signals: cos(0.2π*t) and cos(0.02π*t).

You'll notice that the signal with a higher coefficient of t (frequency of 0.1Hz or rad/sec 0.2π) has more rapid changes, while in the other signal (with a frequency of 0.01Hz), the rate of change is slower.

If we assume these two above signals are respectively the signals sent to the Snape and Gryffindor offices, then the signal you receive from the phone line should be the sum of these two signals, resulting in you receiving the lower-frequency signal.

![Alt text](https://github.com/CP-NIT/Final-Project/blob/main/s1_2.png)

To separate two signals with different frequencies that are present in one signal, we can use a filter. By passing the input signal through an appropriate filter, we can separate two signals with different frequencies from each other.

#### Filter ?? What's that?

Well, in simple terms, filters are systems that allow a signal to pass through them, letting a part of the signal through and blocking the rest.

One common classification of filters is as follows:
- High-pass filter
- Band-pass filter
- Low-pass filter

Where the high-pass filter allows a portion of the signal with a frequency higher than a specific frequency to pass through, the band-pass filter allows a portion of the signal within the frequency range from f_0 to f_1 to pass through, and the low-pass filter allows a portion of the signal with a frequency lower than a specific frequency to pass through.

Now, what exactly does this filter look like??

In discrete form, this filter is an array of numbers. All you need to do is perform the convolution operation on the input signal, which is provided to you discretely, and implement the appropriate filter. For this task, first implement a function that performs the convolution operation, then pass the filter and signal as inputs to that function.

#### Problem Statement

In your program, receive the signal.
Implement the convolution function.
Find the appropriate filter.
Perform convolution of the signal with the appropriate filter and separate the signals for the two offices separately in the output.

### Question 2 – Quidditch Competition

#### Part 1: Harry Potter and his friends want to participate in this year's Quidditch competition. However, the unique aspect of this year's competition is that to make it more challenging, the university officials have decided to place charged points at various locations on the playing field.

Harry Potter and his friends want to become the champions this year, so they asked you to write a program to find the electric field resulting from these charges at a point of their choosing.

Your program is supposed to receive a two-dimensional array representing the playing field, where points with charges are indicated by the value of the charge they hold. One element of the array is represented by the letter 'O', and your program should calculate the electric field at point O and display it in the output. To do this, create a function that takes an array as input and returns a list with two elements, representing the magnitude of the field in the x and y directions, respectively.

For example, your input might be:


#### Part 2: Hagrid, who has a great fondness for straight lines, after hearing about your program, asks you to calculate the electric field at a distance of one meter from the center of a 50-meter straight line with a uniform charge density of 1C.

### Question 3 – Smart Attendance System

Dumbledore wants to design an intelligent attendance system using artificial intelligence, but he realizes that he needs an edge detection system for this purpose. He has heard that by applying two-dimensional convolution on an image with an appropriate filter, this task can be accomplished. Since you have implemented a function for the convolution operation effectively, he asks you to do this task for him.

Our requirements from you are:
1. Read the image file and convert it into a two-dimensional array.
2. Create a function that takes a two-dimensional array as an image and another two-dimensional array as a filter, performs two-dimensional convolution on these two, and returns the result of this operation.
3. Find the appropriate filter for edge detection.
4. Perform the convolution operation on the image and filter, and display the result in the output.

### Optional Task 1 - Hogwarts Electrical Wiring

This extra section is worth 2 additional points for the project.

Dumbledore wants to wire Hogwarts for electricity. For this purpose, he uses a three-phase transformer to deliver power to consumers. The transformer type is EI and its inputs are primary and secondary voltages and currents. Your task is to calculate the core cross-sectional area based on the specified power and current density, and calculate the number of turns of primary and secondary based on input and output voltages. Dumbledore gives you the initial problem statement, and you should find the correct solution with appropriate coding. Depending on the situation and encountered problems, Dumbledore may ask you to simultaneously solve both tasks or only one of them. Sometimes, due to his age and absent-mindedness, Dumbledore may make a mistake, and your code should be able to respond to Dumbledore at any time.

### Optional Task 2 - Dumbledore and His Strange Requests

This extra section is worth 2 additional points for the project.

Dumbledore, in order to encourage people to go to Hogwarts, asks you to make your code user-friendly using a GUI and gain people's trust through Unit Tests.

Implementation of a Graphical User Interface (GUI): Implement a graphical user interface using Tkinter or PyQt (it must show input signals and signals sent to each office).

Unit Test: Create comprehensive tests to ensure the correctness and reliability of project calculations and functionalities.
