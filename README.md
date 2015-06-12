# pyrel  @EdwinMrqz
a python karel like program

This is a karel like program:<br>
You take control over a robot and give it instructions, to walk around a map in which there could be walls
the goal is to implement a complete language but it is still missing some parts, (and the map creator)

-------
<h4> Instructions: </h4>
First, start play.py <br>
on unix-like systems: *python play.py [file with instructions]*<br>
![Pyrel start](/screenshots/pyrel_0.png)
If you specify a file with instructions they are going to be loaded in the text area
rigth now there are only few instructions:<br>
	 1. *move*<br>
	 2. *lookUp* <br>
	 3. *turnRight*<br>
	 4. *lookDown*<br>
	 5. *putItem*<br>
	 6. *pickItem*<br> <br>

	 7. *isWallInfront* <br>
	 8. *isWallAtRight* <br>
	 9: *isWallBehind*  <br>
	10: *isWallAtLeft*  <br>
	11: *isOverItem*    <br>
	12: *hasItem*       <br>


![Pyrel writec](/screenshots/pyrel_1.png)

After you have wrote your program you can start it and wait for it to execute

![Pyrel execute](/screenshots/pyrel_2.png)