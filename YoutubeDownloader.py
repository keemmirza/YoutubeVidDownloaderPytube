from pytube import YouTube

#Simple Python Projects that shows on how to use the pytube Library
#Author : keemmirza

url = input("Insert Youtube Video URL : ")
#Getting YouTube URL from User

utube = YouTube(url)
#Initialize YouTube object with the YouTube URL


print("Title : ",utube.title)
#Shows the title of the YouTube video

print("Video Length : ",utube.length)
#Shows the duration of the YouTube video

print("Total Views : ",utube.views)
#Shows the total views of the YouTube video

print("Video Rating : ",utube.rating)
#Shows the rating of the YouTube video

utubedonlod=utube.streams.get_highest_resolution()
#Getting the Youtube video with the highest resolution into an object

print("Downloading...")
#Print "Downloading..." while the file is downloading in the background

utubedonlod.download()
#Downloding the YouTube video using the object that has been created on line 25

print("Download Completed")
#Print "Download Completed" when the above line has finished eexecuted

#Future enhancement :
#1. Add others functionalities in the pytube library
#2. Creating more robust program which take into account such as download failure
# or WIFI/Internet Connection DNS blocks YouTube website