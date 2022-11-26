"""
File: webcrawler.py
Name: A-Bu
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        tags = soup.find_all("tr")
        male_num = 0
        female_num = 0
        for tag in tags:
            # Filter the text not the rank
            if tag.text.split("\n")[0].isdigit():
                name_num_lst = (tag.text.split("\n")[1]).split(" ")    # The list of the names and numbers

                male_number_lst = name_num_lst[1].split(",")    # Pick up the male's number and remove the comma
                male_number_lst.reverse()    # Put the smaller digit in the front
                male_num += sum(int(male_number_lst[i]) * (1000 ** i) for i in range(len(male_number_lst)))
                female_number_lst = name_num_lst[3].split(",")
                female_number_lst.reverse()
                female_num += sum(int(female_number_lst[i]) * (1000 ** i) for i in range(len(female_number_lst)))

        print(f"Male Number: {male_num}")
        print("Female Number:", female_num)


if __name__ == '__main__':
    main()
