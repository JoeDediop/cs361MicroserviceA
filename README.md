# Microservice A
Communication Contract:
a) Instructions to REQUEST Data from the Microservice
Example:

Request Format: Write "run, amount=X" to request.txt, where X is the number of names requested.
Example Call:

run, amount=5

b) Instructions to RECEIVE Data from the Microservice
Response Format: The microservice will replace the contents of request.txt with a semicolon-separated list of names. So your main program will need to wait for the Microservice to make changes before pulling the new data its replaced with.
Example Call:
Vorlyn, Zorreth, Malara, Lyrreth, Elalyn

c) UML Diagram
![image](https://github.com/user-attachments/assets/26e16fc6-f278-4cc1-b697-1fc7eace22d8)

d) Additional Details
- Agree that the REQUESTING program will use the format "run, amount=X" with X being the amount of names requested. 
- This Microservice was written with the assumption that the microservice is always watching request.txt for changes, so they will share file locations.
- Note about file paths or directory requirements: however your files are handled, this microservice was written under the assumption that it shares a file location with 'request.txt'

Mitigation Plan

For which teammate did you implement “Microservice A”?
 - Teammate: Auberon.

What is the current status of the microservice?
 - Status: Complete and functional.

How is your teammate going to access your microservice?

 - The microservice and instructions for usage are in the GitHub repository. My teammate can download or clone the repo and run the microservice locally.

If your teammate cannot access/call YOUR microservice, what should they do?

 - via our Discord channel or my school email.

Availability: 

 - For quick responses, within 12 hours of messaging on Discord. For emails or larger messages, expect a delay of 24 hours. 

If your teammate cannot access/call your microservice, by when do they need to tell you?

 - ASAP, at least 72 hours before it is required for assignment turn in. Anything less may not be possible due to performing my own tasks.

Anything else your teammate needs to know?

 - Nope, everything else should be covered here! 
