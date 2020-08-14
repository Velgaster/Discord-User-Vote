# Discord-User-Vote
A Discord bot to keep server chats friendly based on uservotes and blacklists.

# Setup
###clone the repo
```
git clone https://github.com/Velgaster/Discord-User-Vote
cd Discord-User-Vote
```

###set up the python virtual environment
#####Linux
```
python3 -m venv venv
source venv/bin/activate
pip install -U -r requirements.txt
```
#####Windows
Make sure python3.x is your default system interpreter.
```
python -m venv venv
venv\Scripts\activate.bat
pip install -U -r requirements.txt
```
 

(optional) to keep the bot up after detaching the terminal, you can use `screen` on debian-based systems
```
sudo apt-get install screen
```

Next, [Set up your bot-account](https://discord.com/developers/applications) and add it to your server.

In `cogs/scripts/settings.py` place the `TOKEN` and `OWNER_ID`

# Usage
make sure the venv is active. 

To do so run `source venv/bin/activate` on Linux or `venv\Scripts\activate.bat` on Windows.


run the bot with `screen` as background task:
```
screen python client.py
```
if you close the terminal, the bot will still run as a process.

to get back to the bot process after reopening your terminal, use:
```
screen -rd
```

run the bot without `screen`:
```
python client.py
```
note that without `screen` (or an equivalent), the bot stops running if you close your terminal or ssh session.



## to do list
- storing the token etc encrypted
- multi-server support