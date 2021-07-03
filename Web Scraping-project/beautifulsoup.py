from re import I
from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/")
data=response.text
soup=BeautifulSoup(data,"html.parser")


movie_names_list=soup.find_all(name="h3",class_="title")


final_output=[]
for i in range(len(movie_names_list)-1,-1,-1):
    movie=(movie_names_list[i]).get_text()
    final_output.append(movie)


with open("movies_names.txt","w") as file:
    for movie in final_output:
        file.write(movie + "\n")
