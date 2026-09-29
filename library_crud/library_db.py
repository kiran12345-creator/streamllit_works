import mysql.connector

class BookListCreateRetrieveDeleteUpdate:
    def __init__(self):
        self.con = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='library_db')
        print(self.con)
        self.cursor=self.con.cursor()
        print('sucessfully connected')
    def list(self):
        query='select * from book'
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
        #     for row in records:
            return(records)
        else:
            print('no records found')
    def create(self,title,author,price,language,pages):
        query='insert into book(title,author,price,language,pages) values(%s,%s,%s,%s,%s);'
        data=(title,author,price,language,pages)
        self.cursor.execute(query,data)
        self.con.commit()
        print('inserted data sucessfully')
    def retrieve(self,id):
        query='select * from book where id = %s'
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            return(record)
        else:
            print('no record found')
    def delete(self,id):
        query='delete from book where id=%s;'
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
             return False


    def update(self,id,title,author,price,language,pages):
        query='update book set title=%s,author=%s,price=%s,language=%s,pages=%s where id = %s'
        data=(title,author,price,language,pages,id)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False

b=BookListCreateRetrieveDeleteUpdate()
b.list()
#b.create('abc','kiran',230,'eng',500)
# b.retrieve((1,))
#b.delete((1,))