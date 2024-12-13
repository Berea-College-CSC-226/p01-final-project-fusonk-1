# CSC226 Final Project

## Instructions

️**Author(s)**: Kirsten Fuson

**Google Doc Link**: https://docs.google.com/document/d/1K2Ult_9eZ7bWyDMxQHnbboVqMiqreudtSwFlgg9h9ko/edit?usp=sharing

---

## References 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update as you go.
https://www.pygame.org/docs/ref/display.html
https://www.pygame.org/docs/ref/sprite.html
https://github.com/search?q=pygame.sprite.collide_rect+language%3APython&type=Code&l=Python
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.kill
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.collide_rect
https://www.pygame.org/docs/ref/time.html#pygame.time.delay
str(self.player.hp) - converting a int into a string for display - Professor Hegan
The legend of Tuna game we worked on in class
https://www.youtube.com/watch?v=4TfZjhw0J-8 - sprite groups explained
https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.Sprite.groups
https://docs.python.org/3/library/time.html
hhttps://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks
https://www.pygame.org/docs/ref/time.html#pygame.time.delay
https://www.pygame.org/docs/ref/time.html
https://www.pygame.org/docs/ref/tests.html
https://www.pygame.org/docs/ref/image.html#pygame.image.load - images for sprites
https://www.youtube.com/watch?v=6tNS--WetLI - testing
---

## Milestone 1: Setup, Planning, Design

️**Title**: `The Creatures’ Keep`

**Purpose**: `My project will be like a dungeon crawler. I want it to be a game where you fight monsters, get treasure, and move to the next level until the character either dies, or the player makes it out with all their gold.`

**Source Assignment(s)**: `T11(The Legends of Tuna: Breath of Catnip),t12(Events and GUIs), T01(Choose Your Own Adventure), HW07(The Game of Nim)`

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:
  
![](image/Class_Dungeon.png)
![](image/Class_Item.png)
![](image/Class_Monster.png)
![](image/Class_Player.png)
![](image/Class_RunGame.png)

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments: 

```
    Branch 1 name: fusonk
    Branch 2 name: _____________
```
---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    **Currently, I feel like Im behind. I know my game seems like its going to be pretty big, so im just going to try and slow it down. By that I mean I will focus on
    one class at a time, and make sure the most important parts of the game are working before I move on. Im honestly suprised by how much goes into a game that at first glance
    would feel pretty simple, but then you look at everything that goes into that kinda game, and its a lot of code being used to make it happen, even for the more simple things.
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `45%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    **I don't feel confident about finishing everything that I wanted to do with this assignment. I took on a lot, and
    the code was ended up being more complicated to implement, which I knew it was going to be. Some strategies to increase the likeleyhood I'll be
    successful in completing the project are by lowering the scope of my project. By that I mean to do what is necessary to get the code working and worry about
    the look and feel a bit after. Maybe doing something more like stages rather than seperate rooms, such as having monsters spawn after each stage, and having a 
    the death be the end of the game, or a set number of monsters you have to fight to win. I will also work on it a bit more over the weekend, aswell as the week coming up.
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions
You can move the character using the arrows, you can click on the chest by getting close to it and pressing a.
This will add the gold to your total in the bottom part of the screen. You want to avoid the ball that is spawned every
5 seconds by the monster, if it hits you you will take one damage. You have 5 hearts so you can take 5 hits. You can also
see this next to the gold in the bottom of the screen. You can hit the monster by going close to hit and hitting f two times, this
will kill the monster and give you additional gold, it will also reload the chest, and make it full of gold
again. The monster will respawn, and the game ends when you run out of hearts.

### Reflection

I selected my project, because I enjoy games and I wasn't great at coding so I wanted to take on
a bigger project in order to try and increase my skills, while learning how to create games, because
I enjoy making games. I knew this would be hard to create, and it has been. My final project is a bit different from
what I was originally planning to create, I've had to change where some items run because they were game mechanics
not sprite mechanics. I've had to overhaul how the sprites work by turning them into groups. The game
overall has become more of an arcade type game where your going for the most gold until your character dies.

I think the hardest part about the final project was figuring out how to kill sprites.
Originally they weren't grouped, so even though I knew about the kill method I had no idea how to implement it, until
after I had watched a video on it to try and figure out my issue. Im also having trouble killing the attack sprites
that I've had to respawn, so currently they are a game feature to make the game end quicker.

I certainly haven't been able to do everything I wanted to, but I don't regret trying to
make a small dungeon crawler, because I feel like I've learned so much.
I've learned how to handle sprite collisions better, how to group sprites, how to call on classes 
from different code pages, learn what should be game code vs what should be sprite code,
how to create sprites, how to add text to the screen when its updating, and Im even starting to learn how tick speed works,ect.

Next time, I think I would work on getting tick speed down, so that I could use it for collisions instead
of the delay that is causing the whole screen to freeze. I would also like to learn how to kill old sprite
after getting a new one, because the old one just sits on the screen and does nothing except be a small issue for
the player.