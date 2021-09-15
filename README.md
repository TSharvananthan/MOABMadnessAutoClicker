# BTD 5 MOAB Madness Auto Clicker
The first coding projects that I was genuinely proud of. This project purely exists on my GitHub as a sign of progress and to demonstrate the intuition that was behind this project and what early 2019 Thanussian was thinking.

## Overview
Too say the least... *phew*; it has been nearly three years since I began learning Python. To say the least, the journey has been fun and I've enjoyed every step that's led to this point. Moreover, there's still a long journey ahead. I'd like to say that I've just begun applying my programming skills to the real world. 

Anyways, onto this program.

## What Is This? 
This program is an auto clicker that played through a specific level of [Bloons Tower Defense 5](https://store.steampowered.com/app/306020/Bloons_TD_5/), a tower defense game that pits you as the overseer of an army of monkeys that have to pop a series of balloons. 

## How Did You Do This? 
This program was written using the `pyautogui` module and uses exact coordinates to click on certain parts of the screen during certain times. 

At the time I didn't know about Github or scalable code. The only reason why I made this program was for my own benefit.

So I opened up a seperate terminal, went into a Python shell and typed in `pyautogui.displayMousePosition()`.

Using that, I manually went to every button that I needed to click and noted down each coordinate in `cooridnates(RAWNOTES).txt`

With that, I implemented the appropriate clicks and pauses in `moabmadnessautoclicker.py`

## How Could I Improve This Program?
- For a more scalable experiance, I could create formulas based off the current coordinates (since I have the exact screen size of the given coordinates) and base the coordinates accordingly
- Make PyAutoGui find the .exe file that runs when the game is run.
- Use libraries that have more a focus on controlling the .exe then a module like `pyautogui` that purely focuses on automated clicking
