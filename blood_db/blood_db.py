import mysql.connector

class DonorListCreateRetrieveDeleteUpdate:
    def __init__(self):
        self.con = mysql.connector.connect(
            user='root',
            password='root',
            host='localhost',
            database='blood_db')
        print(self.con)
        self.cursor=self.con.cursor()
        print('sucessfully connected')

    def list(self):
        query='select * from donor'
        self.cursor.execute(query)
        records=self.cursor.fetchall()
        if records:
            return(records)
        else:
            print('no records found')

    def create(self,name,blood_group,phone,city,last_donation):
        query='insert into donor(name,blood_group,phone,city,last_donation) values(%s,%s,%s,%s,%s);'
        data=(name,blood_group,phone,city,last_donation)
        self.cursor.execute(query,data)
        self.con.commit()
        print('inserted data sucessfully')

    def retrieve(self,id):
        query='select * from donor where id = %s'
        data=(id,)
        self.cursor.execute(query,data)
        record=self.cursor.fetchone()
        if record:
            return(record)
        else:
            print('no record found')

    def delete(self,id):
        query='delete from donor where id=%s;'
        data=(id,)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False

    def update(self,id,name,blood_group,phone,city,last_donation):
        query='update donor set name=%s,blood_group=%s,phone=%s,city=%s,last_donation=%s where id = %s'
        data=(name,blood_group,phone,city,last_donation,id)
        self.cursor.execute(query,data)
        self.con.commit()
        if self.cursor.rowcount>0:
            return True
        else:
            return False


d=DonorListCreateRetrieveDeleteUpdate()
d.list()
#d.create('Kiran','O+','9876543210','Kochi','2026-09-20')
#d.retrieve(1)
#d.delete(1)
#d.update(1,'Kiran','O+','9876543210','Kochi','2026-09-20')