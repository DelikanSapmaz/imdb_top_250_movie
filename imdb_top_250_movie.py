import requests
from bs4 import BeautifulSoup

class Imdb():
    def __init__(self):
        self.url="https://www.imdb.com/chart/top/"
        self.response=requests.get(self.url)
        self.content=self.response.content
        self.soup=BeautifulSoup(self.content,"html.parser")
        self.titles=self.soup.find_all("td",{"class":"titleColumn"})
        self.raitings=self.soup.find_all("td",{"class":"ratingColumn imdbRating"})
    def top_250_write(self):
        for title,raiting in zip(self.titles,self.raitings):
            title=title.text
            title=title.replace("\n","")
            title=title.strip()

            raiting=raiting.text
            raiting=raiting.replace("\n","")
            raiting=raiting.strip()
            print(title,raiting)
    def rating_range(self):
        rating_range=input("Enter the raiting: ")
        for title,raiting in zip(self.titles,self.raitings):
            title=title.text
            title=title.replace("\n","")
            title=title.strip()

            raiting=raiting.text
            raiting=raiting.replace("\n","")
            raiting=raiting.strip()
            if float(raiting)>float(rating_range):
                print(title,raiting)
      
def show_menu():
    print("""
    1-Top 250 movies
    2-Enter the raiting
    3-Exit
    """)
def restart():
    main()

imdb=Imdb()
def main():
    heal=3
    while True:
        show_menu()
        choice=input("Enter your choice: ")
        if choice=="1":
            imdb.top_250_write()
        elif choice=="2":
            imdb.rating_range()
        elif choice=="3":
            choice=input("Are you sure? (y/n):")
            if choice=="y":
                break
            else:
                restart()
        else:
            heal-=1
            if heal>0:
                print("Wrong choice!")
            else:
                print("You have no more chance!")
                break

main()