# Python Discord Bot Template



## Authors
* **[Marcos Melgar (@imcosmicowl)](https://github.com/imcosmicowl)**

## Support

Before requesting support you should know that this template requires you to have a **basic knowledge** of Python. Do not use this template if you don't know the basics. [Here's](https://pythondiscord.com/pages/resources) a link for resources to learn python.

If you need some help for something, do not hesitate to join my discord server [here](https://discord.gg/HzJ3Gfr).

All the updates of the template are available [here](UPDATES.md).

## How to download it

This repository is now a template, on the top left you can simple click on "**Use this template**" to create a GitHub repository based on this template.

Alternatively you can do the following:
* Clone/Download the repository
    * To clone it and get the updates you can definitely use the command
    `git clone`
* Create a discord bot [here](https://discord.com/developers/applications)
* Get your bot token
* Invite your bot on servers using the following invite:
https://discordapp.com/oauth2/authorize?&client_id=YOUR_APPLICATION_ID_HERE&scope=bot&permissions=8 (Replace `YOUR_APPLICATION_ID_HERE` with the application ID)

## How to setup

To setup the bot I made it as simple as possible. I now created a [config.py](config.py) file where you can put the needed things to edit.

Here is an explanation of what everything is:

| Variable              | What it is                                                            |
| ----------------------| ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE  | The prefix(es) of your bot                                            |
| YOUR_BOT_TOKEN_HERE   | The token of your bot                                                 |
| APPLICATION_ID        | The application ID of your bot                                        |
| OWNERS                | The user ID of all the bot owners                                     |
| BLACKLIST             | The user ID of all the users who can't use the bot                    |

## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows) or your Command Prompt (Windows).

Before running the bot you will need to install all the requirements with this command:
```
pip install -r requirements.txt
```

If you have multiple versions of python installed (2.x and 3.x) then you will need to use the following command:
```
python3 bot.py
```
or eventually
```
python3.8 bot.py
```
<br>

If you have just installed python today, then you just need to use the following command:
```
python bot.py
```

## Built With

* [Python 3.8](https://www.python.org/)

## Issues or Questions

If you have any issues or questions of how to code a specific command, you can:

* Join my discord server [here](https://discord.gg/HzJ3Gfr)
* Post them [here](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/issues)

Me or other people will take their time to answer and help you.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available, see the [tags on this repository](https://github.com/kkrypt0nn/Python-Discord-Bot-Template/tags). 

## Bots who used this template

*DM Krypton#7331 to get yourself in this list*

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
