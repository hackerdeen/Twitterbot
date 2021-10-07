A python twitter robot for tweeting the hackerspace status at [57North Hacklab](https://57north.org.uk)

Set up a venv using requirements.txt, ask hibby for the credentials file, go ham.

When setting up on a new machine remember to:

`pip3 install -r requirements.txt`

also don't forget 
```
sudo cp tweetbot.service /etc/systemd/system/tweetbot.service
sudo systemctl daemon-reload
sudo systemctl enable tweetbot
sudo systemctl start tweetbot
```
