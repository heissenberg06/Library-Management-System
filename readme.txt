icons.rc.py comes from icons.qrc file because to execute the application
python could be see the qrc file. Thanks to the transformation, python
can execute the icons. to do this, we use that command : pyrcc5 icons.qrc -o icons_rc.py