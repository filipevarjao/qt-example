# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Tue Feb 28 10:18:37 2012
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 662)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.name_label = QtGui.QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(40, 47, 62, 20))
        self.name_label.setObjectName("name_label")
        self.name = QtGui.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(110, 40, 401, 31))
        self.name.setObjectName("name")
        self.path_label = QtGui.QLabel(self.centralwidget)
        self.path_label.setGeometry(QtCore.QRect(40, 80, 62, 17))
        self.path_label.setObjectName("path_label")
        self.form = QtGui.QLabel(self.centralwidget)
        self.form.setGeometry(QtCore.QRect(30, 20, 71, 21))
        self.form.setObjectName("form")
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 10, 401, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.path = QtGui.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(110, 70, 401, 31))
        self.path.setObjectName("path")
        self.initials_label = QtGui.QLabel(self.centralwidget)
        self.initials_label.setGeometry(QtCore.QRect(30, 110, 62, 17))
        self.initials_label.setObjectName("initials_label")
        self.initials = QtGui.QLineEdit(self.centralwidget)
        self.initials.setGeometry(QtCore.QRect(110, 100, 401, 31))
        self.initials.setObjectName("initials")
        self.workload_label = QtGui.QLabel(self.centralwidget)
        self.workload_label.setGeometry(QtCore.QRect(10, 137, 91, 21))
        self.workload_label.setObjectName("workload_label")
        self.workload = QtGui.QLineEdit(self.centralwidget)
        self.workload.setGeometry(QtCore.QRect(110, 130, 401, 31))
        self.workload.setObjectName("workload")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 170, 71, 20))
        self.label.setObjectName("label")
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 10, 231, 31))
        self.comboBox.setObjectName("comboBox")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 160, 401, 101))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 339, 781, 291))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.submit = QtGui.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(190, 270, 81, 31))
        self.submit.setObjectName("submit")
        self.abort = QtGui.QPushButton(self.centralwidget)
        self.abort.setGeometry(QtCore.QRect(270, 270, 81, 31))
        self.abort.setObjectName("abort")
        self.enviroment = QtGui.QPushButton(self.centralwidget)
        self.enviroment.setGeometry(QtCore.QRect(10, 310, 201, 27))
        self.enviroment.setObjectName("enviroment")
        self.course = QtGui.QPushButton(self.centralwidget)
        self.course.setGeometry(QtCore.QRect(210, 310, 201, 27))
        self.course.setObjectName("course")
        self.discipline = QtGui.QPushButton(self.centralwidget)
        self.discipline.setGeometry(QtCore.QRect(410, 310, 191, 27))
        self.discipline.setObjectName("discipline")
        self.gang = QtGui.QPushButton(self.centralwidget)
        self.gang.setGeometry(QtCore.QRect(600, 310, 191, 27))
        self.gang.setObjectName("gang")
        self.edit = QtGui.QPushButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(110, 270, 81, 31))
        self.edit.setObjectName("edit")
        self.checkBox_initials = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_initials.setGeometry(QtCore.QRect(510, 100, 94, 31))
        self.checkBox_initials.setText("")
        self.checkBox_initials.setObjectName("checkBox_initials")
        self.checkBox_workload = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_workload.setGeometry(QtCore.QRect(510, 130, 94, 31))
        self.checkBox_workload.setText("")
        self.checkBox_workload.setObjectName("checkBox_workload")
        self.checkBox_description = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_description.setGeometry(QtCore.QRect(510, 190, 94, 31))
        self.checkBox_description.setText("")
        self.checkBox_description.setObjectName("checkBox_description")
        self.checkBox_path = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_path.setGeometry(QtCore.QRect(510, 70, 94, 31))
        self.checkBox_path.setText("")
        self.checkBox_path.setObjectName("checkBox_path")
        self.checkBox_name = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_name.setGeometry(QtCore.QRect(510, 40, 94, 31))
        self.checkBox_name.setText("")
        self.checkBox_name.setObjectName("checkBox_name")
        self.checkBox_form = QtGui.QCheckBox(self.centralwidget)
        self.checkBox_form.setGeometry(QtCore.QRect(510, 10, 94, 31))
        self.checkBox_form.setText("")
        self.checkBox_form.setObjectName("checkBox_form")
        self.submit_ok = QtGui.QPushButton(self.centralwidget)
        self.submit_ok.setGeometry(QtCore.QRect(350, 270, 81, 31))
        self.submit_ok.setObjectName("submit_ok")
        self.remove = QtGui.QPushButton(self.centralwidget)
        self.remove.setGeometry(QtCore.QRect(430, 270, 91, 31))
        self.remove.setObjectName("remove")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("MainWindow", "Nome", None, QtGui.QApplication.UnicodeUTF8))
        self.path_label.setText(QtGui.QApplication.translate("MainWindow", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.form.setText(QtGui.QApplication.translate("MainWindow", "Formulário", None, QtGui.QApplication.UnicodeUTF8))
        self.initials_label.setText(QtGui.QApplication.translate("MainWindow", "Iniciais", None, QtGui.QApplication.UnicodeUTF8))
        self.workload_label.setText(QtGui.QApplication.translate("MainWindow", "Carga Horária", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Descrição", None, QtGui.QApplication.UnicodeUTF8))
        self.submit.setText(QtGui.QApplication.translate("MainWindow", "Novo", None, QtGui.QApplication.UnicodeUTF8))
        self.abort.setText(QtGui.QApplication.translate("MainWindow", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.enviroment.setText(QtGui.QApplication.translate("MainWindow", "Coligados", None, QtGui.QApplication.UnicodeUTF8))
        self.course.setText(QtGui.QApplication.translate("MainWindow", "Cursos", None, QtGui.QApplication.UnicodeUTF8))
        self.discipline.setText(QtGui.QApplication.translate("MainWindow", "Disciplina", None, QtGui.QApplication.UnicodeUTF8))
        self.gang.setText(QtGui.QApplication.translate("MainWindow", "Turmas", None, QtGui.QApplication.UnicodeUTF8))
        self.edit.setText(QtGui.QApplication.translate("MainWindow", "Editar", None, QtGui.QApplication.UnicodeUTF8))
        self.submit_ok.setText(QtGui.QApplication.translate("MainWindow", "Ok", None, QtGui.QApplication.UnicodeUTF8))
        self.remove.setText(QtGui.QApplication.translate("MainWindow", "Remover", None, QtGui.QApplication.UnicodeUTF8))

