from PySide2 import QtWidgets
import form
import pickle


class Book:
    def __init__(self, name, author, status, remarks, path):
        self.name = name
        self.author = author
        self.status = status
        self.remarks = remarks
        self.path = path


def add():
    n = input("add book name:   ")
    a = input("add book author:   ")
    s = input("add book status:   ")
    r = input("add book remarks:   ")
    p = input("add book path:   ")

    book = Book(name=n if n != '' else 'Undefined',
                author=a if a != '' else 'Undefined',
                status=s if s != '' else 'Undefined',
                remarks=r if r != '' else 'Undefined',
                path=p if p != '' else 'Undefined')

    print(book.name, book.author, book.status, book.remarks, book.path)

    pickle_in = open('list.pickle', 'rb')
    pickle_list = pickle.load(pickle_in)
    pickle_list.append(book)

    pickle_out = open('list.pickle', 'wb')
    pickle.dump(pickle_list, pickle_out)
    pickle_out.close()


def remove(x):
    pickle_in = open('list.pickle', 'rb')
    pickle_list = pickle.load(pickle_in)

    for i, o in enumerate(pickle_list):
        if o.name == x:
            del pickle_list[i]
            break

    pickle_out = open('list.pickle', 'wb')
    pickle.dump(pickle_list, pickle_out)
    pickle_out.close()


def edit(e):
    pickle_in = open('list.pickle', 'rb')
    pickle_list = pickle.load(pickle_in)

    for i, o in enumerate(pickle_list):
        if o.name == e:
            o.name = input("add book name:   ")
            o.author = input("add book author:   ")
            o.status = input("add book status:   ")
            o.remarks = input("add book remarks:   ")
            o.path = input("add book path:   ")
        print(o.name, o.author, o.status, o.remarks, o.path)

    pickle_out = open('list.pickle', 'wb')
    pickle.dump(pickle_list, pickle_out)
    pickle_out.close()


def read():
    pickle_in = open('list.pickle', 'rb')
    new_loaded_list = pickle.load(pickle_in)
    for i in new_loaded_list:
        print(i.name, i.author, i.status, i.remarks, i.path)


# add()
# read()
# remove(input('type book name to remove:   '))
# edit(input('type book name to edit:   '))
# read()


class MyQtApp(form.Ui_graphics, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Mindgarden')
        self.treeWidget.itemClicked.connect(self.item2Clicked)
        self.pushButton.clicked.connect(self.addbtn)
        self.pushButton_2.clicked.connect(self.rmvbtn)
        self.pushButton_3.clicked.connect(self.edtbtn)

        self.main_tree_widget()

    def main_tree_widget(self):
        self.treeWidget.clear()
        self.treeWidget.setSortingEnabled(True)

        pickle_in = open('list.pickle', 'rb')
        new_loaded_list = pickle.load(pickle_in)

        for i in new_loaded_list:
            #self.rem = i.remarks
            # print(i.name, i.author, i.status, i.remarks, i.path)
            item = QtWidgets.QTreeWidgetItem(self.treeWidget, [i.name, i.author, i.status, i.path, i.remarks])
            # print(item.text(4))

    def item2Clicked(self, item):
        self.textBrowser.clear()
        self.textBrowser.append(item.text(4))
        print(item.text(2))


    def addbtn(self):
        j = QtWidgets.QTreeWidgetItem(self.treeWidget, ['carr', '0.99', 'Fff', 'ggg', 'tttt'])
        self.treeWidget.addTopLevelItem(j)
        print('addbtn')

    def rmvbtn(self):
        pass

        # self.treeWidget.itemClicked.
        # print(item)

    def edtbtn(self):
        print('edtbtn')

    # a = QtWidgets.QTreeWidgetItem(self.treeWidget, ['carr', '0.99', 'Fff', 'ggg'])
    # self.treeWidget.removeItemWidget(a, 0)


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
