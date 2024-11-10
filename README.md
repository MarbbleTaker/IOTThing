What Project does: 

Raspberry Pi Pico W microcontroller is used as the central control unit in the IoT project. It is connected to three input buttons and an output buzzer for creating an interactive guessing game. The buttons give inputs in which the user can adjust or submit their guesses to the system. They are connected to the GPIO pins of the Pico and configured to detect when a press happens. This press can be used to control actions of the game, such as increasing the guessed frequency or confirming the guess. 
 
This is the main output transducer: it provides audible feedback to the user by means of a buzzer. It's connected to a GPIO pin so the Pico can change the frequency of the buzzer. This feature is used to play different tones as cues, such as whether the user is right or wrong. All these inputs and outputs together form a complete system where users can interact through the buttons, and the buzzer acts as responses to create a simple yet engaging IoT device. 

Project Purpose: 

The purpose of this IoT project is to create an interactive guessing game using a Raspberry Pi Pico W microcontroller. In this game, users try to match randomly generated frequencies by adjusting and submitting their guesses through buttons. The buzzer provides audio cues to indicate whether the guess is correct or incorrect. This project demonstrates the use of sensor inputs and transducer outputs to create a responsive and engaging IoT device. 

Project Setup: 

Microcontroller: The Raspberry Pi Pico W serves as the central control unit. 

Inputs: Three buttons are connected to the GPIO pins on the Pico, enabling users to adjust or submit their frequency guesses. 

Output: A buzzer is connected to the GPIO, allowing the Pico to emit tones of varying frequencies as feedback. 

Wiring: All components (buttons, buzzer, wires) are set up on a breadboard, with proper connections to the Pico’s GPIO pins. 

Usage: 

Adjusting the Guess: Users press the first button to increase or decrease their frequency. 

Confirming the Guess: The second button is used to submit or confirm the guess. 

Feedback from the Buzzer: After each guess, the buzzer plays a tone to indicate whether the guess was correct (matching the random frequency) or incorrect. The feedback helps guide users to the correct answer by adjusting their next guesses. 

This setup provides an engaging and interactive experience where users can interact with an IoT system to play a guessing game, while also gaining insight into how microcontrollers, sensors, and transducers can be combined to create functional projects. 
