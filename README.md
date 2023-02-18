# BBDC TPDS Bot (Deprecated)
By Jonathan Ngien

# Description

### Background: 
In order to obtain a driving license in Singapore, one would have to complete a driving simulator course, comprising of 3 seperate sessions, in order to be qualified to take the practical exam. However, due to an overwhelming surge in competitiveness in searching for Traffic Police Driving Simulator (TPDS) Slots at Bukit Batok Driving Centre (BBDC), in addition to the fact that students are only able to book a slot after they had attended their current lesson, it takes an average of 6-8 months for a student to finish their simulator lessons. 

This situation is aggravated due to the COVID-19 restrictions (as of 2021) as proper safe distancing measurers are in place. As of April 2021, the earliest slot is in July 2021 (3 months of waiting time).

As a result of waiting 6 - 9 months to finish their TPDS course, students will have to continually take up more driving lessons during this time to ensure they remain proficient and prepared for their practical driving test. As for students who want to search for slots manually, which the bot aims to overcome, they spend hours and hours of their time in search for an earlier slot.

### Solution
Fortunately, students are able to cancel their slots should they be unable to make it for a class. As a result, if one were to constantly refresh the page, they would eventually manage to find a slot that has been cancelled, days or even weeks earlier than the ones readily available.

### Code
- Implemented the Selenium Framework together with Python to navigate HTML pages
- Included Telegram's API that sends a notification to user's Telegram account informing them when a slot has been found or if the program has stopped running.
