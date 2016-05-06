# my_first_calculator.py
I initially saw [Al Sweigart](https://github.com/asweigart)'s [my_first_tic_tac_toe](https://github.com/asweigart/my_first_tic_tac_toe) and was amused. I then saw the image shown below posted on Reddit. Assuming that the image was not made up for some fake internet points and also assuming that their friend only used addition, subtraction, multiplication and division then the number of numbers that they would have if statements for would be...

    sqrt(9500/4) = 48.7339...
    sqrt(9500/4) ≈ 50 

So to be true to the "real" story I have only gone from 0-50 however higher numbers can easily be generated too however my Python crashes with larger numbers. I generated one that was 0-1000 and it took up 317 MB of space on my hard drive but was only 20MB after I compressed it to a .rat so I have also attached it.

The generator will not work in Python 2 it can easily be patched to work by putting a ".0" on the end of the eval and then cutting off the last two when printing the equation but I decided to not do what because it would add a ".0" to the end of additions, subtractions and multiplications (or you could use an if statement but I decided to miss that out).

![The image](https://i.imgur.com/ZMvUovj.png)
