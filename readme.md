## Setup Instructions
### For linux:
#### If you have docker:
1. Open the terminal in the project directory then run the commands 
2. ``` chmod +x run_services.sh $$ chmod +x stop_services.sh  ```
3. ``` run_services.sh ```
4. to stop just run : ``` stop_services.sh ```
#### If you do not have docker:
1. Follow this [tutorial](https://www.geeksforgeeks.org/how-to-setup-rabbitmq-in-linux-server/
    ) to setup and run RabbitMQ
2. ```python3 -m venv venv```
    ```source venv/bin/activate``` 
3. ``` pip install --upgrade pip ```
        ``` pip install -r requirements.txt ```
4. Run the services :
```sudo gnome-terminal -- bash -c "python3 services/api_service/api_service.py; exec bash" & sudo gnome-terminal -- bash -c "python3 services/filter_service/filter_service.py; exec bash" & sudo gnome-terminal -- bash -c "python3 services/screaming_service/screaming_service.py; exec bash" & sudo gnome-terminal -- bash -c "python3 services/publish_service/publish_service.py; exec bash"```
- **To use the smtp server for sending emails**:
Enable Two-Factor Authentication (if not already enabled):
1. Go to Google Account Security Settings.
   - Turn on 2-Step Verification.
2. Generate an App Password:
   - After enabling 2FA, go to the App Passwords page.
   - Select the app (Mail) and device (Custom Name, e.g., Publish Service).
   - Click "Generate" to get a 16-character app password.
   - Update the SMTP Credentials: Replace the password in your service configuration with the app password.
3. Put your Email and App password in publish service and put all emails you want to send for them 

 ### For windows:
 1. install the  RabbitMQ server or run it using docker 
 2. source the virtual environment 
 3. install the dependencies 
 4. run the services 

## Tests {#tests}
**1. Correct message**
```curl -X POST -H "Content-Type: application/json" -d '{"alias": "user1", "text": "This is a valid message!"}' http://127.0.0.1:5000/submit_message```
- Expected:
    - Filter Service:
        - Log: "Received message: {'alias': 'user1', 'text': 'This is a valid message!'} 
        Filter Service: Message passed the filter and will be forwarded."
        - Forwarding to the next service

    - Screaming Service:
        - Log: "SCREAMING Service: Received message: {'alias': 'user1', 'text': 'This is a valid message!'} 
        SCREAMING Service: Converted message to uppercase: {'alias': 'user1', 'text': 'THIS IS A VALID MESSAGE!'}"
        - Forwarding to the next service

    - Publish Service:
        - Log: "Received message: {"alias": "user1", "text": "THIS IS A VALID MESSAGE!"}
        Email sent successfully!"

**2. Filtered word**
```curl -X POST -H "Content-Type: application/json" -d '{"alias": "user1", "text": "I love mango smoothies!"}' http://127.0.0.1:5000/submit_message ```
- Expected:
  - Filter Service:
    - Log: "Filter Service: Received message: {'alias': 'user1', 'text': 'I love mango smoothies!'}
    Filter Service: Message contains stop words and will be dropped: I love mango smoothies!"
    - Message is not forwarded further, so no logs should be displayed in the screaming, publish services.

**3. Invalid data (not enough fields)**
```curl -X POST -H "Content-Type: application/json" -d '{"alias": "user1"}' http://127.0.0.1:5000/submit_message```
- Expected:
  - API service:
    - Log: "127.0.0.1 - - [27/Nov/2024 19:10:30] "POST /submit_message HTTP/1.1" 400"
    - No other logs or actions should be displayed.

**4. Empty message**
```curl -X POST -H "Content-Type: application/json" -d '{"alias": "user1", "text": ""}' http://127.0.0.1:5000/submit_message```
- Expected:
  - Filter Service:
    - Log: "Received message: {'alias': 'user1', 'text': ''}
    Filter Service: Message passed the filter and will be forwarded."
    - Forwarding to the next service

  - Screaming Service:
    - Log: "SCREAMING Service: Received message: {'alias': 'user1', 'text': ''}
    SCREAMING Service: Converted message to uppercase: {'alias': 'user1', 'text': ''}"
    - Forwarding to the next service

  - Publish Service:
    - Log: "Received message: {'alias': 'user1', 'text': ''}
    Email sent successfully!"

## Run pipes-and-filters
1. Move to the project's <i>pipes_and_filters</i> directory
2. Run ```python test_filters.py```
3. In separate window you can test it using <a href="#tests">Tests</a>, no need for RabbitMQ
