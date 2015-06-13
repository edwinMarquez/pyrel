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
rigth now there are only these instructions:<br>
	 1. *move*<br>
	 2. *lookUp* <br>
	 3. *turnRight*<br>
	 4. *lookDown*<br>
	 5. *putItem*<br>
	 6. *pickItem*<br> <br>
	 Control Expresions <br><br>
	 7. *repeat n times* (any level of anidation )<br>
	 8. *repeatEnd*<br>
	 Boolean Expresions <br><br>
	 9. *isWallInfront* <br>
	10. *isWallAtRight* <br>
	11: *isWallBehind*  <br>
	12: *isWallAtLeft*  <br>
	13: *isOverItem*    <br>
	14: *hasItem*       <br>


![Pyrel writec](/screenshots/pyrel_1.png)

After you have wrote your program you can start it and wait for it to execute

![Pyrel execute](/screenshots/pyrel_2.png)