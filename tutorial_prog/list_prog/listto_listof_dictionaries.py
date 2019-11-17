color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
my_zip = zip(color_name,color_code)
for a,b in my_zip:
    c = [{'color_name':a,'color_code':b}]
    print(c)

