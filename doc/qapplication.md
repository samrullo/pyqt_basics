# QApplication

- Your application needs one and only one version of QApplication
- Event loop is owned by QApplication

```python
1 fromPyQt5.QtWidgetsimport*
2 fromPyQt5.QtCoreimport*
3 fromPyQt5.QtGuiimport*
4
5 #Onlyneededforaccesstocommandlinearguments
6 importsys
7
8 #Youneedone(andonlyone)QApplicationinstanceperapplication.
9 #Passinsys.argvtoallowcommandlineargumentsforyourapp.
10 #Ifyouknowyouwon'tusecommandlineargumentsQApplication([])workstoo.
11 app=QApplication(sys.argv)
12
13 #Starttheeventloop.
14 app.exec_()
15 16
17 #Yourapplicationwon'treachhereuntilyouexitandtheevent
18 #loophasstopped.

```