from bs4 import BeautifulSoup

# OPENING AND READING FILE
with open("home.html", 'r') as html_file:
    content = html_file.read()
    
    # CREATING A BEAUTIFULSOUP OBJECT
    soup = BeautifulSoup(content, 'lxml')
    courses_cards = soup.find_all("div", class_="card") # class is a reserved keyword in python so we use class_
    print(courses_cards)
    for course in courses_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # split() returns list of words, we get last word which is price
        # print(course.a.text)
        print(f"{course_name} costs {course_price}")