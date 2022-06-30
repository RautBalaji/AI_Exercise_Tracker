# AI_Exercise_Tracker
<h1>Instruction </h1>

1.download assignment folder

2.put kneebendvideo.mp4 file you have in the folder (https://drive.google.com/drive/folders/1cAH7tfvGg3ka0bos1Dorc4n7WmubjqlV?usp=sharing)

2.run knee_bend.py file

<h1>Problem Statement</h1>
We have track knee bend pose.
create a trigger mechanism when knee went down befor 8 sec display a warning message.
create counter which count no of raps.




<h1>Output</h1>



https://user-images.githubusercontent.com/104637675/176600696-ace21adf-03fb-4200-b861-309fb5fab8b4.mp4



<h1>Process:</h1>

1.create a pose module to detect pose  

     1.1 find the ladmarks only for left knee(hip,knee,ankle)
  
     1.2 find the angle bew landmarks


2.convert min and max angle between 0-100 percent

3.check weather angle <140
     3.1 start timer
  
     3.2 increase counter

4.check weather angle>140

    4.1 check time >8 if yes continue
  
    4.2 check time <8 if yes print("bend your knees") and decrease the counter as raps not complete(try to overcome fluctuated frame problem)

5.print counter and raps 
