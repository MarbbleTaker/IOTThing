What it does: 

 

Raspberry Pi Pico W microcontroller is used as the central control unit in the IoT project. It is connected to three input buttons and an output buzzer for creating an interactive guessing game. The buttons give inputs in which the user can adjust or submit their guesses to the system. They are connected to the GPIO pins of the Pico and configured to detect when a press happens. This press can be used to control actions of the game, such as increasing the guessed frequency or confirming the guess. 
 
This is the main output transducer: it provides audible feedback to the user by means of a buzzer. It's connected to a GPIO pin so the Pico can change the frequency of the buzzer. This feature is used to play different tones as cues, such as whether the user is right or wrong. All these inputs and outputs together form a complete system where users can interact through the buttons, and the buzzer acts as responses to create a simple yet engaging IoT device. 
