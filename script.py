import sqlite3

def search(string):
    conn = sqlite3.connect("assignment.db")
    cursor = conn.cursor()

    if string.strip() == "":
        print("Please enter a search string.")
        return


    query = "SELECT name, marks FROM students WHERE LOWER(name) LIKE ?"
    cursor.execute(query, ('%' +string.lower() + '%',))
    rows = cursor.fetchall()

  
    total_marks = 0
    average_marks = 0.0
    num_rows = len(rows)

    if num_rows > 0:
        for row in rows:
            name, marks = row
            print("Name: {}, Marks: {}".format(name, marks))
            total_marks += marks
        average_marks = total_marks / float(num_rows) 
        print("Total Marks: {}".format(total_marks))
        print("Average Marks: {}".format(average_marks))
    else:
        print("No matching records found.")


    conn.close()


def main():
    while True:
        search_string = raw_input("Enter search string (or 'exit' to quit): ").strip()

        if search_string.lower() == 'exit':
            print("Exiting the program.")
            break
        
        search(search_string)

if __name__ == "__main__":
    main()
