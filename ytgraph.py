from pytube import Playlist, YouTube, Channel
import matplotlib.pyplot as plt

link = "https://www.youtube.com/watch?v=phV8GqKPXLo&list=PLhpi7wXTY-5w4I8XxD9P1tCMJOMLfcVdM"
def main(mod,link):
  channel = "channel"
  playlist = "playlist"

  if mod == channel:
    x = Channel(link)
  elif playlist:
    x = Playlist(link)
    
  views = []
  dates = []
  #print(x.views)
  sum = 0

  for video in x.videos:
    views.append(video.views)
    dates.append(video.publish_date)
    #print("Next")
    sum+=video.views

  print(sum)


  plt.plot(dates,views)

  plt.show()
main("channel","https://www.youtube.com/c/ERL%C4%B0K61")
