import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
     '''
     MainWindow
     '''
     def __init__(self):
         '''
         __init__ method
         '''
         super(MainWindow, self).__init__()
         self.setFixedSize(1360, 768)
         self.mdi = QMdiArea()
         self.mdi.setFixedSize(1343, 770)
         self.Ui()

     def Ui(self):
         '''
         MainWindow user interface constructor
         '''
         Menu = self.menuBar()
         dbMenu = QMenu('Databases', self)
         self.dbsearchItem = QAction('Search database', self)
         dbMenu.addAction(self.dbsearchItem)
         uMenu = QMenu('Users', self)
         self.UsearchItem = QAction('Search User', self)
         self.UnewItem = QAction('New User', self)
         self.UupdtItem = QAction('Update User', self)
         self.UdropItem = QAction('Drop User', self)
         uMenu.addAction(self.UsearchItem)
         uMenu.addAction(self.UnewItem)
         uMenu.addAction(self.UupdtItem)
         uMenu.addAction(self.UdropItem)
         dptMenu = QMenu('Departments', self)
         self.deptsearchItem = QAction('Search Department', self)
         dptMenu.addAction(self.deptsearchItem)
         sessionMenu = QMenu('Session', self)
         self.logoffItem = QAction('Log off', self)
         sessionMenu.addAction(self.logoffItem)
         Menu.addMenu(dbMenu)
         Menu.addMenu(uMenu)
         Menu.addMenu(dptMenu)
         Menu.addMenu(sessionMenu)
         self.dbsearchItem.triggered.connect(self.subwinDatabases)
         self.UsearchItem.triggered.connect(self.subwinUsers)
         self.UnewItem.triggered.connect(self.subwinNewUser)
         self.UupdtItem.triggered.connect(self.subwinUpdtUser)
         self.UdropItem.triggered.connect(self.subwinDropUser)
         self.deptsearchItem.triggered.connect(self.subwinDepartments)
         self.logoffItem.triggered.connect(self.close)
         self.layout = QVBoxLayout()
         self.layout.addWidget(Menu)
         self.layout.addWidget(self.mdi)
         widget = QWidget()
         widget.setLayout(self.layout)
         self.setCentralWidget(widget)

     def subwinDatabases(self):
         '''
         'Database' instantiation
         '''
         instance = Databases()
         subwindow = self.mdi.addSubWindow(instance)
         subwindow.setFixedSize(410, 350)
         subwindow.setWindowFlags(Qt.FramelessWindowHint)
         subwindow.move(5,5)
         subwindow.show()

     def subwinUsers(self):
         '''
         'Users' instantiation
         '''
         instance = Users()
         subwindow = self.mdi.addSubWindow(instance)
         subwindow.setFixedSize(740, 350)
         subwindow.setWindowFlags(Qt.FramelessWindowHint)
         subwindow.move(5,360)
         subwindow.show()

     def subwinNewUser(self):
         '''
         'New User' instantiation
         '''
         instance = NewUser()
         subwindow = self.mdi.addSubWindow(instance)
         subwindow.setFixedSize(400, 350)  # x, y
         subwindow.setWindowFlags(Qt.FramelessWindowHint)
         subwindow.move(100, 360)  # x, y
         subwindow.show()

     def subwinUpdtUser(self):
         '''
         'Update User' instantiation
         '''
         instance = UpdtUser()
         subwindow = self.mdi.addSubWindow(instance)
         subwindow.setFixedSize(400, 350)  # x, y
         subwindow.setWindowFlags(Qt.FramelessWindowHint)
         subwindow.move(100, 360)  # x, y
         subwindow.show()

     def subwinDropUser(self):
         '''
         'Drop User' instantiation
         '''
         instance = DropUser()
         subwindow = self.mdi.addSubWindow(instance)
         subwindow.setFixedSize(400, 350)  # x, y
         subwindow.setWindowFlags(Qt.FramelessWindowHint)
         subwindow.move(100, 360)  # x, y
         subwindow.show()

     def subwinDepartments(self):
         '''
         'Departments' instantiation
         '''
         instance = Departments()
         subwindow = self.mdi.addSubWindow(instance)
         subwindow.setFixedSize(400, 300)  # x, y
         subwindow.setWindowFlags(Qt.FramelessWindowHint)
         subwindow.move(500, 5)  # x, y
         subwindow.show()


class Databases(QWidget):
    '''
    'Databases' window
    '''
    def __init__(self):
         super(Databases, self).__init__()
         # Label
         self.label = QLabel(self)
         self.label.setGeometry(20, 15, 80, 40)  #    x, y, length, width
         self.label.setText('Database name:')
         self.label.setAlignment(Qt.AlignCenter)
         self.label.setStyleSheet('font-size:11px')
         # Line Edit
         self.dbnamebox = QLineEdit(self)
         self.dbnamebox.setGeometry(110, 20, 120, 25)   #    x, y, length, width
         self.dbnamebox.setStyleSheet('font-size:11px')
         # 'Add' and 'Drop' buttons are enabled as the user types in QLineEdit field:
         self.dbnamebox.textChanged[str].connect(lambda: self.dbnewbtn.setEnabled(self.dbnamebox.text() != ""))
         self.dbnamebox.textChanged[str].connect(lambda: self.dbdropbtn.setEnabled(self.dbnamebox.text() != ""))
         # 'Search' Button
         self.dbsearchbtn = QPushButton(self)
         self.dbsearchbtn.setGeometry(240, 20, 70, 25) #    x, y, length, width
         self.dbsearchbtn.setStyleSheet('font-size:11px')
         self.dbsearchbtn.setText('Search')
         # 'Add' Button
         self.dbnewbtn = QPushButton(self)
         self.dbnewbtn.setGeometry(315, 20, 70, 25) #    x, y, length, width
         self.dbnewbtn.setStyleSheet('font-size:11px')
         self.dbnewbtn.setText('Add new')
         self.dbnewbtn.setDisabled(True) # button is enabled as the user types in QLineEdit field
         # 'Drop' Button
         self.dbdropbtn = QPushButton(self)
         self.dbdropbtn.setGeometry(305, 305, 85, 25) #    x, y, length, width
         self.dbdropbtn.setStyleSheet('font-size:11px')
         self.dbdropbtn.setText('Drop database')
         self.dbdropbtn.setDisabled(True) # button is enabled as the user types in QLineEdit field
         # 'Database query' Table
         self.dbqrytable = QTableWidget(self)
         self.dbqrytable.setGeometry(20, 60, 365, 230)  #    x, y, length, width
         self.dbqrytable.setStyleSheet('font-size:11px')
         self.dbqrytable.setColumnCount(2)
         self.dbqrytable.setRowCount(10)
         self.dbqrytable.setHorizontalHeaderLabels(['Name','Size'])
         self.dbqrytable.horizontalHeader().setStretchLastSection(True)
         self.dbqrytable.clearContents() # shows a clear table on startup
         self.dbqrytable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # read-only data
         # Button 'on click' events:
         self.dbsearchbtn.clicked.connect(self.dbsearchQuery)
         self.dbnewbtn.clicked.connect(self.dbnewQuery)
         self.dbdropbtn.clicked.connect(self.dbdropQuery)

    def dbsearchQuery(self):
        '''
        (1) connects to the database, (2) the query returns searched database name --
        it will return an empty table if no matches were found, (3) collects the text written
        in the QLineEdit widget, (4) then compares to each row in the database,
        (5) generates a buffer of results, (6) collects the number of rows in the buffer,
        (7) collects the number of columns in the buffer, (8) allows sorting by clicking in the
        header, (9) allows 10 rows to be displayed only, (10) allows 2 columns to be displayed only,
        (11) the for-loop fills in the QTableWidget with results of the query
        '''
        import psycopg2 as pg2
        connection = pg2.connect(
            host='localhost',
            database='',
            user='postgres',
            password='ThomasKaufmann001')
        connection.autocommit = True
        cursor = connection.cursor() # 1
        query = """ (SELECT datname, pg_size_pretty(pg_database_size(%s))
                    FROM pg_database
                    WHERE datname = %s)
                    UNION (SELECT null, null) LIMIT 1;
                """ # 2
        db_name = self.dbnamebox.text()  # 3
        cursor.execute(query,(db_name,db_name,)) # 4
        records = cursor.fetchall()  # 5
        rows = len(records)  # 6
        columns = len(records[0]) # 7
        self.dbqrytable.setSortingEnabled(True)  # 8
        self.dbqrytable.setRowCount(10)  # 9
        self.dbqrytable.setColumnCount(2)  # 10
        for i in range(rows):  # 12
            for j in range(columns):
                item = QTableWidgetItem(records[i][j])
                self.dbqrytable.setItem(i, j, item)

    def dbnewQuery(self):
        '''
        query implemented using 'SQLAlchemy' instead of 'psycopg2' library
        '''
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        db_name = self.dbnamebox.text()
        engine = create_engine('postgresql+psycopg2://postgres:ThomasKaufmann001@localhost/')
        session = sessionmaker(bind=engine)()
        session.connection().connection.set_isolation_level(0)
        # To avoid duplicated database names,
        # the new database is created only if it doesn't already exist:
        exists = session.execute(""" SELECT * FROM pg_database WHERE datname = '{}'; """.format(db_name)).fetchone()
        if not exists:
            query = """ CREATE DATABASE {};                                
                    """.format(db_name)
            session.execute(query)
            session.connection().connection.set_isolation_level(1)

    def dbdropQuery(self):
        '''
        query implemented using 'SQLAlchemy' instead of 'psycopg2' library
        '''
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        db_name = self.dbnamebox.text()
        engine = create_engine('postgresql+psycopg2://postgres:ThomasKaufmann001@localhost/')
        session = sessionmaker(bind=engine)()
        session.connection().connection.set_isolation_level(0)
        query = """
                DROP DATABASE IF EXISTS {};
                """.format(db_name)
        session.execute(query)
        session.connection().connection.set_isolation_level(1)


class Users(QWidget):
    '''
    'Users' window
    '''
    def __init__(self):
         super(Users, self).__init__()
         # 'Option' Label
         self.optionbox = QComboBox(self)
         self.optionbox.setGeometry(20, 20, 80, 25)  # x, y, length, width
         self.optionbox.addItems(['emp_no','birth_date', 'first_name', 'last_name', 'gender', 'hire_date'])
         self.optionbox.setStyleSheet('font-size:11px')
         # 'Query' Line Edit
         self.querybox = QLineEdit(self)
         self.querybox.setGeometry(110, 20, 120, 25)  # x, y, length, width
         self.querybox.setStyleSheet('font-size:11px')
         # 'Search' button is enabled as the user types in QLineEdit field:
         self.querybox.textChanged[str].connect(lambda: self.Usearchbtn.setEnabled(self.querybox.text() != ""))
         # 'Search' Button
         self.Usearchbtn = QPushButton(self)
         self.Usearchbtn.setGeometry(240, 20, 70, 25) #    x, y, length, width
         self.Usearchbtn.setStyleSheet('font-size:11px')
         self.Usearchbtn.setText('Search')
         self.Usearchbtn.setDisabled(True)  # button is enabled as the user types in QLineEdit field
         # 'Add user' Button
         self.Unewbtn = QPushButton(self)
         self.Unewbtn.setGeometry(105, 305, 70, 25) #    x, y, length, width
         self.Unewbtn.setStyleSheet('font-size:11px')
         self.Unewbtn.setText('Add user')
         # 'Update user' Button
         self.Uupdtbtn = QPushButton(self)
         self.Uupdtbtn.setGeometry(205, 305, 85, 25) #    x, y, length, width
         self.Uupdtbtn.setStyleSheet('font-size:11px')
         self.Uupdtbtn.setText('Update user')
         # 'Drop user' Button
         self.Udropbtn = QPushButton(self)
         self.Udropbtn.setGeometry(305, 305, 85, 25) #    x, y, length, width
         self.Udropbtn.setStyleSheet('font-size:11px')
         self.Udropbtn.setText('Drop user')
         # 'User query' Table
         self.Uqrytable = QTableWidget(self)
         self.Uqrytable.setGeometry(20, 60, 700, 230)  #    x, y, length, width
         self.Uqrytable.setStyleSheet('font-size:11px')
         self.Uqrytable.setColumnCount(6)
         self.Uqrytable.setRowCount(0)  # shows a clear table on startup
         self.Uqrytable.setHorizontalHeaderLabels(['Emp Nr','Birth Date','First Name','Last Name','Gender','Hire Date'])
         self.Uqrytable.horizontalHeader().setStretchLastSection(True)
         self.Uqrytable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers) # read-only data
         # Sub windows list
         self.subwinNewUser = NewUser()
         self.subwinUpdtUser = UpdtUser()
         self.subwinDropUser = DropUser()
         # Button 'on click' events:
         self.Usearchbtn.clicked.connect(self.UsearchQuery)
         self.Unewbtn.clicked.connect(self.subwinNewUser.show)
         self.Uupdtbtn.clicked.connect(self.subwinUpdtUser.show)
         self.Udropbtn.clicked.connect(self.subwinDropUser.show)

    def UsearchQuery(self):
        '''
        (1) connects to the database, (2) the query returns searched user name --
        it will return an empty table if no matches were found, (3) collects the text written
        in the QLineEdit widget, (4) then compares to each row in the database,
        (5) generates a buffer of results, (6) collects the number of rows in the buffer,
        (7) collects the number of columns in the buffer, (8) allows sorting by clicking in the
        header, (9) allows 10 rows to be displayed only, (10) allows 6 columns to be displayed only,
        (11) the for-loop fills in the QTableWidget with results of the query
        '''
        import psycopg2 as pg2
        import datetime
        connection = pg2.connect(
            host='localhost',
            database='Employees',
            user='postgres',
            password='ThomasKaufmann001')
        connection.autocommit = True
        cursor = connection.cursor() # 1
        # Runs the SQL query if the value in QLineEdit is not null:
        try:
            option = self.optionbox.currentText()
            value = self.querybox.text()
            query = """ SELECT TO_CHAR(emp_no,'999999'), TO_CHAR(birth_date,'YYYY-MM-DD'), first_name, 
                               last_name, gender, TO_CHAR(hire_date,'YYYY-MM-DD') 
                        FROM employees
                        WHERE {} = '{}';
                    """.format(option,value)
            cursor.execute(query)
            records = cursor.fetchall()  # 5
            rows = len(records)  # 6
            columns = len(records[0]) # 7
            self.Uqrytable.setSortingEnabled(True)  # 8
            self.Uqrytable.setRowCount(rows)  # 9
            self.Uqrytable.setColumnCount(6)  # 10
            for i in range(rows):  # 11
                for j in range(columns):
                    item = QTableWidgetItem(records[i][j])
                    self.Uqrytable.setItem(i, j, item)
        # Otherwise does nothing:
        except IndexError:
            self.Uqrytable.setRowCount(0)


class NewUser(QWidget):
    '''
    'New User' form subwindow
    '''
    def __init__(self):
        super(NewUser, self).__init__()
        # 'U_ID' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 15, 80, 40)  # x, y, length, width
        self.label.setText('User ID:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'U_ID' Line Edit
        self.UIDbox = QLineEdit(self)
        self.UIDbox.setGeometry(110, 20, 120, 25)  # x, y, length, width
        self.UIDbox.setStyleSheet('font-size:11px')
        self.UIDbox.textChanged[str].connect(lambda: self.dobbox.setEnabled(self.UIDbox.text() != ""))
        # 'birth_date' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 45, 80, 40)  # x, y, length, width
        self.label.setText('Birth date:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'birth_date' Line Edit
        self.dobbox = QLineEdit(self)
        self.dobbox.setGeometry(110, 50, 120, 25)  # x, y, length, width
        self.dobbox.setStyleSheet('font-size:11px')
        # LineEdit is enabled as the user types in previous QLineEdit field
        self.dobbox.setDisabled(True)
        self.dobbox.textChanged[str].connect(lambda: self.fnamebox.setEnabled(self.dobbox.text() != ""))
        # 'first_name' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 75, 80, 40)  # x, y, length, width
        self.label.setText('First name:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'first_name' Line Edit
        self.fnamebox = QLineEdit(self)
        self.fnamebox.setGeometry(110, 80, 120, 25)  # x, y, length, width
        self.fnamebox.setStyleSheet('font-size:11px')
        self.fnamebox.setDisabled(True)
        self.fnamebox.textChanged[str].connect(lambda: self.lnamebox.setEnabled(self.fnamebox.text() != ""))
        # 'last_name' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 105, 80, 40)  # x, y, length, width
        self.label.setText('Last name:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'last_name' Line Edit
        self.lnamebox = QLineEdit(self)
        self.lnamebox.setGeometry(110, 110, 120, 25)  # x, y, length, width
        self.lnamebox.setStyleSheet('font-size:11px')
        self.lnamebox.setDisabled(True)
        self.lnamebox.textChanged[str].connect(lambda: self.genderbox.setEnabled(self.lnamebox.text() != ""))
        # 'gender' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 135, 80, 40)  # x, y, length, width
        self.label.setText('Gender:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'gender' Line Edit
        self.genderbox = QLineEdit(self)
        self.genderbox.setGeometry(110, 140, 120, 25)  # x, y, length, width
        self.genderbox.setStyleSheet('font-size:11px')
        self.genderbox.setDisabled(True)
        self.genderbox.textChanged[str].connect(lambda: self.hdatebox.setEnabled(self.genderbox.text() != ""))
        # 'hire_date' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 165, 80, 40)  # x, y, length, width
        self.label.setText('Hire date:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'hire_date' Line Edit
        self.hdatebox = QLineEdit(self)
        self.hdatebox.setGeometry(110, 170, 120, 25)  # x, y, length, width
        self.hdatebox.setStyleSheet('font-size:11px')
        self.hdatebox.setDisabled(True)
        self.hdatebox.textChanged[str].connect(lambda: self.Unewbtn.setEnabled(self.hdatebox.text() != ""))
        # 'Add' Button
        self.Unewbtn = QPushButton(self)
        self.Unewbtn.setGeometry(305, 305, 85, 25)  # x, y, length, width
        self.Unewbtn.setStyleSheet('font-size:11px')
        self.Unewbtn.setText('Add user')
        self.Unewbtn.setDisabled(True)  # button is enabled as the user types in QLineEdit field
        # Button 'on click' events:
        self.Unewbtn.clicked.connect(self.UnewQuery)
        self.Unewbtn.clicked.connect(self.close)

    def UnewQuery(self):
        '''
        'Add new user' query
        '''
        import psycopg2 as pg2
        U_ID = self.UIDbox.text()
        birth_date = self.dobbox.text()
        first_name = self.fnamebox.text()
        last_name = self.lnamebox.text()
        gender = self.genderbox.text()
        hire_date = self.hdatebox.text()
        with pg2.connect(
            host='localhost',
            database='Employees',
            user='postgres',
            password='ThomasKaufmann001') as connection:
                connection.autocommit = True
                # To avoid duplicated U_ID codes,
                # the new U_ID code is created only if it doesn't already exist:
                with connection.cursor() as cursor:
                    cursor.execute(""" SELECT * FROM employees WHERE emp_no = '{}'; """.format(str(U_ID)))
                    exists = cursor.fetchall()
                    if not exists:
                        query = """ 
                                INSERT INTO employees(emp_no, birth_date, first_name, last_name, 
                                                      gender, hire_date)
                                VALUES ('{}','{}', '{}', '{}', '{}', '{}');
                                """.format(str(U_ID), str(birth_date), str(first_name), str(last_name),
                                           str(gender), str(hire_date))
                        with connection.cursor() as cursor:
                            cursor.execute(query)
        self.UIDbox.clear()
        self.dobbox.clear()
        self.fnamebox.clear()
        self.lnamebox.clear()
        self.genderbox.clear()
        self.hdatebox.clear()


class UpdtUser(QWidget):
    '''
    'Update User' form subwindow
    '''
    def __init__(self):
        super(UpdtUser, self).__init__()
        # 'U_ID' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 15, 80, 40)  # x, y, length, width
        self.label.setText('User ID:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'U_ID' Line Edit
        self.UIDbox = QLineEdit(self)
        self.UIDbox.setGeometry(110, 20, 120, 25)  # x, y, length, width
        self.UIDbox.setStyleSheet('font-size:11px')
        # 'Option' Label
        self.optionbox = QComboBox(self)
        self.optionbox.setGeometry(20, 75, 80, 20)  # x, y, length, width
        self.optionbox.addItems(['birth_date','first_name','last_name','gender','hire_date'])
        self.optionbox.setStyleSheet('font-size:11px')
        # 'NewValue' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 105, 80, 40)  # x, y, length, width
        self.label.setText('New value:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'NewValue' Line Edit
        self.newvaluebox = QLineEdit(self)
        self.newvaluebox.setGeometry(110, 110, 120, 25)  # x, y, length, width
        self.newvaluebox.setStyleSheet('font-size:11px')
        # 'Search' button is enabled as the user types in QLineEdit field:
        self.newvaluebox.textChanged[str].connect(lambda: self.Uupdtbtn.setEnabled(self.newvaluebox.text() != ""))
        # 'Update' Button
        self.Uupdtbtn = QPushButton(self)
        self.Uupdtbtn.setGeometry(305, 305, 85, 25)  # x, y, length, width
        self.Uupdtbtn.setStyleSheet('font-size:11px')
        self.Uupdtbtn.setText('Update user')
        self.Uupdtbtn.setDisabled(True)  # button is enabled as the user types in QLineEdit field
        # Button 'on click' events:
        self.Uupdtbtn.clicked.connect(self.UupdtQuery)
        self.Uupdtbtn.clicked.connect(self.close)

    def UupdtQuery(self):
        '''
        'Update user' query
        In an attempt to update an user whose U_ID doesn't exist, the function
        will not work but no message error is shown.
        '''
        import psycopg2 as pg2
        U_ID = self.UIDbox.text()
        option = self.optionbox.currentText()
        newvalue = self.newvaluebox.text()
        with pg2.connect(
            host='localhost',
            database='Employees',
            user='postgres',
            password='ThomasKaufmann001') as connection:
                connection.autocommit = True
                query = """ 
                        UPDATE employees 
                        SET {} = '{}' 
                        WHERE emp_no = {};   
                        """.format(option, newvalue, str(U_ID))
                with connection.cursor() as cursor:
                    cursor.execute(query)
        self.UIDbox.clear()
        self.newvaluebox.clear()


class DropUser(QWidget):
    '''
    'Drop User' form subwindow
    '''
    def __init__(self):
        super(DropUser, self).__init__()
        # 'U_ID' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 15, 80, 40)  # x, y, length, width
        self.label.setText('User ID:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'U_ID' Line Edit
        self.UIDbox = QLineEdit(self)
        self.UIDbox.setGeometry(110, 20, 120, 25)  # x, y, length, width
        self.UIDbox.setStyleSheet('font-size:11px')
        # 'Admin Password' Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 300, 90, 40)  # x, y, length, width
        self.label.setText('Admin password:')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:11px')
        # 'Admin Password' Line Edit
        self.AdminPassbox = QLineEdit(self)
        self.AdminPassbox.setGeometry(110, 305, 120, 25)  # x, y, length, width
        self.AdminPassbox.setStyleSheet('font-size:11px')
        # 'Drop' button is enabled as the user types in QLineEdit field:
        self.AdminPassbox.textChanged[str].connect(lambda: self.Udropbtn.setEnabled(self.AdminPassbox.text() != ""))
        # 'Drop User' Button
        self.Udropbtn = QPushButton(self)
        self.Udropbtn.setGeometry(305, 305, 85, 25)  # x, y, length, width
        self.Udropbtn.setStyleSheet('font-size:11px')
        self.Udropbtn.setText('Drop user')
        self.Udropbtn.setDisabled(True)  # button is enabled as the user types in QLineEdit field
        # Button 'on click' events:
        self.Udropbtn.clicked.connect(self.UdropQuery)
        self.Udropbtn.clicked.connect(self.close)

    def UdropQuery(self):
        '''
        'Drop user' query
        '''
        import psycopg2 as pg2
        U_ID = self.UIDbox.text()
        AdminPass = self.AdminPassbox.text()
        with pg2.connect(
            host='localhost',
            database='Employees',
            user='postgres',
            password='ThomasKaufmann001') as connection:
                connection.autocommit = True
                query = """ 
                        DELETE FROM employees  
                        WHERE emp_no = {};   
                        """.format(str(U_ID))
                with connection.cursor() as cursor:
                    cursor.execute(query)
        self.UIDbox.clear()
        self.AdminPassbox.clear()


class Departments(QWidget):
    '''
    'Departments' window
    '''
    def __init__(self):
        super(Departments, self).__init__()
        # Label
        self.label = QLabel(self)
        self.label.setGeometry(20, 20, 70, 40)  #    x, y, length, width
        self.label.setText('Departments')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:10px')
