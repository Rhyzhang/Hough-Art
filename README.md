# Hough Art

# Problem Description:

	The goal of this project was to show how programming and mathematics can merge and create beautiful art that is both visually stunning and pleasing to the eye. To do this Mr. Lin used Hough Transform which is an technique used in computer vision to identify straight lines in a photo. What students tried to do was to be inspired by the newly learned Hough transform to enable themselves to create mathematical art. What this means is that the art created does not need to accurately represent a Hough transformation. We simply used the idea and procedures of a Hough transformation to generate new and unique art. To put it simply, we can do anything we want including changing all the parameters and all the functions being used. Thus, I wanted to create a website that allowed a great user experience for tuning these parameters while also enabling more people to explore programming, math, and art.
  
# Explanation Of Mathematical Functions:

	The mathematical ideas used in this project are the: Hough Transform, Polar coordinates, and Transformations. I will attempt to explain these ideas but since I do not know what I am doing, I would recommend lifting your eyes away from what I am about to write and read qualified articles about the listed topics. I have never officially learned these topics in depth, plus I have no idea what I am doing half the time. Please, proceed with caution.
  
![image](https://user-images.githubusercontent.com/65325330/154397760-9c80efc2-7c79-4a90-8c72-d31258c1ff83.png)
Figure 1 - Credit: Mr. Lin

  The Hough Transformation was/still is a computer vision technique used to find straight lines in an image. For example, in the image shown above (Figure 1) the original gray scale image was converted to white and black pixels, then through the Hough Transform (shown in the middle of the image), the computer was able to calculate the straight lines in the image through the pixel or points of the white and black image. The reason why it is wavy is because the Hough Transform was done in polar coordinates as computer cannot handle the normal y = mx + b  representation of a line. That is because computer can no store a potentially HUGE b value when it has a limited amount of storage. Long story short you basically turn points into lines. Then the lines all intersect, or at least closely intersect, because they share the same m and b. In this process, while in the Hough Space, it turns out these lines look very beautiful. Then we just used transformation to wrap the graph around the origin to create a wonderfully, beautiful, magnificent, awesome, flowery, interesting, you get the point, graph.

# Implementation:

	So how does it work? As previously explained, we took inspiration from the Hough Transform thus, it means if doesn’t really have to be accurate… it’s inspiration not real implementation. Here is what’s going on in the background.
There will be a random input image to use the Hough Transformation on. Alternatively, you can also submit you own image. Then a function will create a Hough Space of that image and out put it as a new image. The new image will also be colored to make it look even more pretty. In the Hough function you can tune all the parameters for fun. For example, instead of using Cos and Sin to calculate our radius how about we use Tanh with hmm… haha Cosh! Keep clicking random to generate random parameters and your basically done.
	Please feel free to use my website. If you want to contribute, please just submit a pull request. 


[hough_art (13)](https://user-images.githubusercontent.com/65325330/154397330-85974206-11c2-4252-8887-2c13c63ffb0b.jpg)
![hough_art (6)](https://user-images.githubusercontent.com/65325330/154397334-82d5b8d8-cc9d-41f5-9416-f588603f1566.jpg)
![hough_art (5)](https://user-images.githubusercontent.com/65325330/154397336-5b3b1955-40e8-4ecf-9333-0fccc28efbeb.jpg)
![hough_art (4)](https://user-images.githubusercontent.com/65325330/154397341-6bc2b505-c933-43b7-98e6-b23001814af7.jpg)
![hough_art (3)](https://user-images.githubusercontent.com/65325330/154397348-5fa4c33d-7ae6-4672-b963-2823eae05448.jpg)
![hough_art (2)](https://user-images.githubusercontent.com/65325330/154397352-c77d3bdb-545d-4a90-a7a5-ed4679140d74.jpg)
![hough_art (12)](https://user-images.githubusercontent.com/65325330/154397356-60c09b7f-ed7d-401c-9613-fc2da4d9b3f6.jpg)
![hough_art (11)](https://user-images.githubusercontent.com/65325330/154397357-50c67b14-f864-4edd-b9ec-6b02c6de565a.jpg)
![hough_art (10)](https://user-images.githubusercontent.com/65325330/154397358-97f81f37-c666-48a1-b8d7-92c4ad44ea17.jpg)
![hough_art (9)](https://user-images.githubusercontent.com/65325330/154397360-e55975f1-460b-42ef-b3cf-74354dde36af.jpg)
![hough_art (8)](https://user-images.githubusercontent.com/65325330/154397362-99d99271-d04d-4169-a2ea-f388a5d93d79.jpg)
![hough_art (7)](https://user-images.githubusercontent.com/65325330/154397363-bffc5be7-2994-49b1-9b7a-e7832509ffa1.jpg)
