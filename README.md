# Space Dodge

A game where you dodge bullets that are coming down from the top of the screen. It is only available on Windows and Mac.

## Description

This is just a pygame project which I followed a [YouTube tutorial](https://www.youtube.com/watch?v=waY3LfJhQLY) to
make.  
I have been adding new features such as sound effects, and lives and will try to add any suggestions!  
Please leave them in [Issues under the "suggestion" tag](https://github.com/Spacexplorer11/Space_Dodge/issues/new?template=feature_request.yml).
If you have **any** feedback please fill out this [survey](https://tally.so/r/mOo7pA)

> [!Note]  
> This project **is** currently in **active development**, I work on it during my free time.  
> Any help would be **greatly appreciated!**  
> Do **not** hesitate to open a pull request. I will review it as fast as possible (1-3 days).  
> If you need help opening a pull request, please
> follow [this link](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
> or watch [this video](https://www.youtube.com/watch?v=nCKdihvneS0).

## Instructions to install the game

The instructions to play the game are in-game.
The first few steps for all OS's are 
1. Download Python from [python.org](https://python.org). **Make sure it is correct for your computer.**
> [!Caution]
> Make sure it is the **official** python site (https://python.org)!
2. Download the zip file from the main page of the repository. [Click the green `Code` button and click
   `Download Zip`](https://github.com/Spacexplorer11/Space_Dodge/archive/refs/heads/main.zip)
3. Extract/unzip the file to a desired location.
4. Open the terminal / command prompt on your computer.

## Please find your OS-specific installation instructions below:


### Windows Installation
After completing the above steps,  
You will need to run `python` in terminal/command prompt on its own and download Python from
the Microsoft store ( it will automatically open a window ) as well as from the website.  
Then type: `pip install pygame` into the terminal to install pygame ( the game engine ). You also need to do `pip install pygame_widgets` separately.  
In the extracted folder, find `main.py`, and run it ( right click and open with python not IDLE )  
You can also right-click it, click `copy path`, go to terminal/command prompt and type `python PATH`. Replace `PATH`
with the path to the file.  

### Mac Installation
After completing the above steps, go to terminal and run these commands consecutively ( one after another ):
- `pip3 install --upgrade pip`
- `python3 -m pip install -U pygame --user`
- `python3 -m pip install -U pygame_widgets --user`  
Then, in the extracted folder, find `main.py`, and run it ( right click and open with python not IDLE )
You can also right-click it, click `copy path`, go to terminal/command prompt and type `python PATH`. Replace `PATH`
with the path to the file.

## What to do if anything goes wrong?
You should [create an issue](https://github.com/Spacexplorer11/Space_Dodge/issues/new?template=help_wanted.yml) and make sure to upload the mylog.log file if available. Make sure to upload screenshots or screen recordings of **any** errors. Thanks!
> [!Tip]
> If you can't find the mylog.log file, then
> you should try opening the `main.py` file in the default `IDLE` ( right click `main.py` and open with python IDLE ), and provide a screenshot of the error message when
> you run it in the `IDLE`, as this will severely help me solve the issue faster.

## Credits

- The first basic concept and code was from a [YouTube tutorial](https://www.youtube.com/watch?v=waY3LfJhQLY).
- After that, 100% of the code was written by me.
- All images were generated using [Leonardo.ai](https://leonardo.ai) and the [Terms of Service](https://leonardo.ai/terms-of-service/) allow commercial use, you can read more [here](https://intercom.help/leonardo-ai/en/articles/8044018-commercial-usage)
- Other media that was used is credited here:
    - The [mini-explosion gif](space_dodge/assets/explosion_gif_frames) when a bullet hits the ground, you can find
      it [here](https://en.picmix.com/stamp/Explode-Digital-Art-2334354)
    - The [mute symbol](space_dodge/assets/mute.png) can be found [here](https://www.flaticon.com/free-icons/silent)
    - The [unmute symbol](space_dodge/assets/unmute.png) can be found [here](https://www.flaticon.com/free-icons/enable-sound)
    - The [x symbol](space_dodge/assets/x_button_icon.png) ( the one to exit the pop-up menus) can be found [here](https://static.vecteezy.com/system/resources/previews/024/780/371/non_2x/red-x-button-icon-sticker-clipart-ai-generated-free-png.png)
    - The [pause button](space_dodge/assets/pause_rectangle.png)
    can be found in the SF Symbols app on Mac (It can be downloaded [here](https://developer.apple.com/sf-symbols/))
    - The [Settings animated icon](space_dodge/assets/settings_icon_frames) [was created by Freepik - Flaticon](https://www.flaticon.com/free-animated-icons/settings)
    - The [Mute icon](space_dodge/assets/mute.png) [was created by Freepik - Flaticon](https://www.flaticon.com/free-icons/silent)
    - The [Unmute icon](space_dodge/assets/unmute.png) [was created by Freepik - Flaticon](https://www.flaticon.com/free-icons/enable-sound)
- All sounds were sourced from [Pixabay](https://pixabay.com) and [Uppbeat](https://uppbeat.io)
   - The [pause music](space_dodge/sounds/background_music/pause_screen/pause_music.mp3) is from uppbeat:   
      https://uppbeat.io/t/aylex/evening-meal  
   - The [main game music](space_dodge/sounds/background_music/background_music.mp3) ( not title screen ) is from uppbeat:  
      https://uppbeat.io/t/qube/play  
   - The other sounds are licensed under the [Pixabay License](https://pixabay.com/service/license-summary/)

## FAQ
- Q: Why does the game freeze when I drag the window?
- A: Unfortunately, this is an **operating system bug** which pauses the main thread when you drag the window, causing the game to freeze.
- Q: Do you/will you ever support Linux?
- A: Unfortunately, we do not support Linux at the moment **however**, we are looking to support it in the *near future*.

## Thanks! 💜
Thank you so much for playing Space Dodge! I'd really appreciate it if you starred my repository!
[Back to the top ^](#space-dodge)
