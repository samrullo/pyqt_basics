# Common widgets

## QComboBox
QComboBox is a drop down list. 

```python
widget=QComboBox()
widget.addItems(["One","Two","Three"])
```

It offers below signals
- currentIndexChanged: notifies that we selected another item in the combo box
and passes the index of the selected item

```python
widget.currentIndexChanged.connect(self.index_changed)
``` 

If we want to intercept the text of the item instead of its index

```python
widget.currentIndexChanged[str].connect(self.index_changed)
```

## QListWidget
