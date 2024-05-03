# Final-Project
### Project Description

This project has been designed and developed for the purpose of teaching and applying electrical engineering concepts. It provides the necessary calculations using the Python programming language. This project is single-authored and presented in person. The total score for this project is 2 marks.

**Note:** Data should be stored in files, and user inputs and outputs should be saved and displayed upon request. Users should have the ability to modify or delete saved inputs and outputs. Proper and appropriate commenting is required. Necessary functions should be defined, and appropriate comments should be provided for each code.

### Question 1 – Hogwarts Phone Line

At Hogwarts University, to facilitate communication between students and their respective group professors, they intend to set up a telephone system. Unfortunately, only one phone line is allocated for the Snape and Gryffindor offices. University officials have asked for your assistance to write a program that receives data sent to this line as input and delivers relevant data for the Snape and Gryffindor offices separately as output.

The only difference between the data sent to these two offices is the frequency of the transmission. The signal you receive is the sum of these two signals.

#### Frequency ?? What is it anyway ??

Well, in a very simple sense, we can say the frequency of a signal is higher when it has more sudden changes. For example, let's consider two signals: cos(0.2π*t) and cos(0.02π*t).

You'll notice that the signal with a higher coefficient of t (frequency of 0.1Hz or rad/sec 0.2π) has more rapid changes, while in the other signal (with a frequency of 0.01Hz), the rate of change is slower.

If we assume these two above signals are respectively the signals sent to the Snape and Gryffindor offices, then the signal you receive from the phone line should be the sum of these two signals, resulting in you receiving the lower-frequency signal.

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

