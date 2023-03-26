import pandas
from tkinter import *
import csv
from datetime import datetime



def available_books_command() :
    available_books_window=Tk()
    available_books_window.title('AVAILABLE BOOKS')
    Label(available_books_window,text='Enter Book Name To Search:').grid(column=0,row=0)
    book_search_entry=Entry(available_books_window,width=50)
    book_search_entry.grid(column=1,row=0)
    def book_available_command() :
        book_search_entry_name=book_search_entry.get()
        book_available_dataframe=pandas.read_csv('available_books')
        result_book_details=book_available_dataframe[book_available_dataframe['BOOK_NAME']==book_search_entry_name.lower()]
        det2=''
        for i in result_book_details.BOOK_NAME :
            det2=i
        book_name_entry.insert(0,det2)
        det2=''
        for i in result_book_details.AUTHOR :
            det2=i
        book_author_entry.insert(0,det2)
        det2=''
        for i in result_book_details.QUANTITY :
            det2=i
        book_quantity_entry.insert(0,det2)
        det2=''
        for i in result_book_details.DELIVERED :
            det2=i
        book_delivered_entry.insert(0,det2)
        det2=''
        for i in result_book_details.AVAILABLE :
            det2=i
        book_available_entry.insert(0,det2)

    Button(available_books_window,text='Search',fg='white',bg='blue',command=book_available_command).grid(column=0,row=1)
    Label(available_books_window,text='Book Name:').grid(column=0,row=2)
    Label(available_books_window,text='Author:').grid(column=0,row=3)
    Label(available_books_window,text='Quantity:').grid(column=0,row=4)
    Label(available_books_window,text='Delivered:').grid(column=0,row=5)
    Label(available_books_window,text='Available:').grid(column=0,row=6)
    book_name_entry=Entry(available_books_window,width=30)
    book_name_entry.grid(column=1,row=2)
    book_author_entry=Entry(available_books_window,width=30)
    book_author_entry.grid(column=1,row=3)
    book_quantity_entry=Entry(available_books_window,width=30)
    book_quantity_entry.grid(column=1,row=4)
    book_delivered_entry=Entry(available_books_window,width=20)
    book_delivered_entry.grid(column=1,row=5)
    book_available_entry=Entry(available_books_window,width=20)
    book_available_entry.grid(column=1,row=6)



tkinter_object=Tk()
tkinter_object.title('MAIN MENU')

def books_delivery_command() :
    books_delivery_window=Tk()
    books_delivery_window.title('Books Delivery Details')

    Label(books_delivery_window,text='Person Name:').grid(row=0,column=0)
    person_name_entry=Entry(books_delivery_window,width=50)
    person_name_entry.grid(row=0,column=1)
    Label(books_delivery_window,text='Book Name:').grid(row=1,column=0)
    book_name_entry=Entry(books_delivery_window,width=50)
    book_name_entry.grid(row=1,column=1)
    Label(books_delivery_window,text='Author Name:').grid(row=2,column=0)
    author_name_entry=Entry(books_delivery_window,width=50)
    author_name_entry.grid(row=2,column=1)
    def submit_button_command() :
        book_name = book_name_entry.get()
        person_name = person_name_entry.get()
        author_name = author_name_entry.get()
        book_details_to_check_dataframe=pandas.read_csv('available_books')
        book_present_or_not_details=book_details_to_check_dataframe[book_details_to_check_dataframe['BOOK_NAME']==book_name.lower()]

        if book_present_or_not_details.size>0 :
            for i in book_present_or_not_details.AVAILABLE :
                available_books=i
            if available_books>0 :
                delivery_date = datetime.now().strftime('%d/%m/%y %H:%M:%S')
                book_present_or_not_details.DELIVERED=book_present_or_not_details.DELIVERED+1
                book_present_or_not_details.AVAILABLE=book_present_or_not_details.AVAILABLE-1
                with open('books_delivery_file', 'a', newline='') as file:
                    header_names = ['AuthorName', 'PersonName', 'BookName', 'Date']

                    the_writer = csv.DictWriter(file, fieldnames=header_names)
                    the_writer.writeheader()
                    the_writer.writerow(
                        {'AuthorName': author_name, 'PersonName': person_name, 'BookName': book_name,
                        'Date': delivery_date})
            else :
                Label(books_delivery_window,text='SORRY! THE BOOKS WITH NAME '+book_name+'ARE TOTAL DELIVERED').grid(column=0,row=4)
        else :
            Label(books_delivery_window,text='SORRY! NO BOOKS WITH THIS NAME IN OUR LIBRARY',fg='red').grid(column=0,row=4)




    Button(books_delivery_window,text='Submit',fg='black',bg='blue',command=submit_button_command).grid(row=3,column=0)

    Button(books_delivery_window,text='Exit',fg='black',bg='blue',command=books_delivery_window.quit).grid(row=3,column=1)






Label(tkinter_object,text='-------LIBRARY MANAGEMENT-------',fg='black',font=('bold',25)).place(x=20,y=50)
Button(tkinter_object,text='Book Delivery',bg='blue',fg='white',command=books_delivery_command).place(x=50,y=100)



def books_given_record_command() :
    books_given_record_window=Tk()
    books_given_record_window.title('Books Given Record')
    Label(books_given_record_window,text='Enter Book Name:').grid(row=0,column=0)
    book_name_entry_to_check=Entry(books_given_record_window,width=30)
    book_name_entry_to_check.grid(row=0,column=1)
    def search_btn_command() :

        book_delivery_dataframe=pandas.read_csv('books_delivery_file')

        book_number_to_check=book_name_entry_to_check.get()
        selected_book_name_details=book_delivery_dataframe[book_delivery_dataframe['BookName']==book_number_to_check]
        for i in selected_book_name_details.BookNumber :
            det=i
        book_author_entry_to_show.insert(0,det)
        det=''
        for i in selected_book_name_details.BookName :
            det=i
        book_name_entry_to_show.insert(0,det)
        det=''
        for i in selected_book_name_details.PersonName :
            det=i
        person_name_entry_to_show.insert(0,det)
        det=''
        for i in selected_book_name_details.Date :
            det=i
        date_time_entry_to_show.insert(0,det)




    Button(books_given_record_window,text='Search',bg='blue',fg='white',command=search_btn_command).grid(row=1,column=0)
 #   Button(books_given_record_window,text='Exit',bg='blue',fg='white',command=books_given_record_window.quit()).grid(row=1,column=1)
    Label(books_given_record_window,text='Author Name:').grid(row=2,column=0)
    book_author_entry_to_show=Entry(books_given_record_window,width=30)
    book_author_entry_to_show.grid(row=2,column=1)
    Label(books_given_record_window,text='Book Name:').grid(row=3,column=0)
    book_name_entry_to_show=Entry(books_given_record_window,width=50)
    book_name_entry_to_show.grid(row=3,column=1)
    Label(books_given_record_window,text='Person Name:').grid(row=4,column=0)
    person_name_entry_to_show=Entry(books_given_record_window,width=50)
    person_name_entry_to_show.grid(row=4,column=1)
    Label(books_given_record_window,text='Book Given Date and Time:').grid(row=5,column=0)
    date_time_entry_to_show=Entry(books_given_record_window,width=50)
    date_time_entry_to_show.grid(row=5,column=1)







Button(tkinter_object,text='Books Given Record',bg='blue',fg='white',command=books_given_record_command).place(x=50,y=150)
Button(tkinter_object,text='Available Books',bg='blue',fg='white',command=available_books_command).place(x=50,y=200)
def new_books_entry_command() :

    new_books_entry_window=Tk()
    new_books_entry_window.title('New Books Entry')
    Label(new_books_entry_window,text='Enter Book Name:').grid(column=0,row=0)
    Label(new_books_entry_window,text='Enter Author Name:').grid(column=0,row=1)
    Label(new_books_entry_window,text='Enter Quantity:').grid(column=0,row=2)
    book_name_entry=Entry(new_books_entry_window,width=30)
    book_name_entry.grid(column=1,row=0)
    book_author_name_entry=Entry(new_books_entry_window,width=30)
    book_author_name_entry.grid(column=1,row=1)
    book_quantity_entry=Entry(new_books_entry_window,width=30)
    book_quantity_entry.grid(column=1,row=2)
    def enter_btn_command() :
        book_name_entry_string=book_name_entry.get()
        book_author_name_entry_string=book_author_name_entry.get()
        book_quantity_entry_number=book_quantity_entry.get()
        with open('available_books', 'a', newline='') as book_file:
            header_names_for_book_file = ['BOOK_NAME','AUTHOR', 'QUANTITY', 'DELIVERED','AVAILABLE']
            writer_for_bool_file = csv.DictWriter(book_file, fieldnames=header_names_for_book_file)
            writer_for_bool_file.writeheader()
            writer_for_bool_file.writerow(
                {'BOOK_NAME':book_name_entry_string.lower(),'AUTHOR':book_author_name_entry_string,'QUANTITY':book_quantity_entry_number,'DELIVERED':0,'AVAILABLE':book_quantity_entry_number}
            )
    Button(new_books_entry_window,text='Enter',fg='black',bg='orange',command=enter_btn_command).grid(column=0,row=3)

Button(tkinter_object,text='New Books Entry',bg='blue',fg='white',command=new_books_entry_command).place(x=50,y=250)

tkinter_object.mainloop()