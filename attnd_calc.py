class student:
    def __init__(self, name, program = "sped"):
        self.name = name
        self.program = program
        
    def attnd_count(name):
        year = {"August": 3, "September": 20, "October": 19, "November": 19, "December": 16, "January": 20, "February": 16, "March":16, "April": 14, "May": 22, "June": 7}
        count = 0
        name_attnd = {}
        print("Press \"q\" to quit anytime")
        current_month = 0

        for month in year:

            res = input(f"{month}> ")
            if res == "q":
                return False
            else:
                try:	
                    count += int(res)
                    current_month +=0
                    name_attnd[month]=res
                    print(f"Total: {count}")
                except:
                    print('use an integer please')
                    res = input(f"{month}> ")
            if year[month] > year[len(year) -1]:
                return False
        print(name_attnd)

name = input('enter name > ')
name = student(name)

name.attnd_count()


