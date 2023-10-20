class Star_Cinema:
    __hall_list=[]

    def  entry_hall(self,hall):
        self.__hall_list.append(hall)
    

class Hall(Star_Cinema):
    
    def __init__(self,rows,cols,hall_no) -> None:
        super().__init__()
        self.seats ={}
        self.__show_list=[]
        self.__rows=rows
        self.cols=cols
        self.__hall_no=hall_no
        star_cinema=Star_Cinema()
        star_cinema.entry_hall(self)
    
    def entry_show(self,id, movie_name, time):
        self.__show_list.append((id,movie_name,time))
        a=[[0 for i in range(self.cols)]for j in range(self.__rows)]
        self.seats[id]=a

    def book_seats(self,id,input_r_c):
        
            row=int (input_r_c[0])
            col=int(input_r_c[1])
            seat=self.seats[id]
            if (row>=0 and  row<len(seat)) and (col>=0 and col<len(seat[0])):  
                if seat[row][col]!=1:
                    seat[row][col]=1
                else:
                    print("seat is not available")
            else:
                print("Invalid row and col")
        
        
    def view_show_list(self):
        for shows in self.__show_list:
            print(f'Movie ID:{shows[0]} Movie Name: {shows[1]} Time: {shows[2]}' )
    def view_available_seats(self,id):
        seats=self.seats[id]
        for i in seats:
            print(i)


star_cinema=Star_Cinema()
hall_x=Hall(5,5,231)
hall_x.entry_show('111',' Piash Jiboner bedona','10 october 2023 Time: 9 Am')
hall_x.entry_show("222",'Redowaner jiboner bedona','10 october 2023 Time: 2 pm')
hall_y=Hall(9,9,456)
hall_y.entry_show('333',' jonmo','10 october 2023 Time: 11 Am')
hall_y.entry_show('444',' Mrittu','10 october 2023 Time: 4 PM')


        
while True:
    print(1,": VIEW ALL SHOW TODAY")
    print(2,": VIEW AVAILABLE SEAT")
    print(3,": BOOK SEAT")
    print(4,":EXIT")
    option=int(input("Choose option:"))
    if option==1:
        hall_x.view_show_list()
        hall_y.view_show_list()

    elif option==2:
        id=input("Enter Movie id:")
        if id in hall_x.seats:
            hall_x.view_available_seats(id)
        elif id in hall_y.seats:
            hall_y.view_available_seats(id)
        else:
            print("NO SUCH MOVIE ID")
        

    elif option==3:
        id=input("Enter Movie id:")
        if id in hall_x.seats:
            n=int(input("How many tickets you want: "))
            while n:
                n-=1
                r=int(input("Enter row:"))
                c=int(input("Enter collam:"))
                hall_x.book_seats(id,(r,c))
        elif id in hall_y.seats:
            n=int(input("How many tickets you want: "))
            while n:
                n-=1
                r=int(input("Enter row:"))
                c=int(input("Enter collam:"))
                hall_y.book_seats(id,(r,c))
        else:
            print("INVALID MOVIE ID")

            

    elif option==4:
        break
    else:
        print("WRONG COMMAND. PLEASE ENTER CORRECTLY")
            

    
