import requests

img_url = "https://scontent.fblr1-4.fna.fbcdn.net/v/t1.0-9/48415821_926557847550612_3082924857894109184_n.jpg?_nc_cat=108&_nc_oc=AQm8sbRK08nmLlxvsk_Y8SY1MRqanr51PlphTPZb73FGefiplg9QPoMElg0i_ZTySI0&_nc_ht=scontent.fblr1-4.fna&oh=b6c2d17cece4b85500406f7702ac366a&oe=5DEA5B74"

a = requests.get(img_url)

with open("venk_pic.img","wb") as my_file:
    my_file.write(a.content)
print("Task Successfully Completed....!!!!")



