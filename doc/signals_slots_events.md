# Signals, Slots, Events

Every interaction the user has with Qt application causes an Event.
There are multiple types of events, each representing different types of interactions.
Events are passed to the event specific handler on the widget where the interaction occurred.
For example clicking a mouse button causes ```QtMouseEvent```
which is handled by ```mousePressEvent``` method of the widget on which mouse was clicked.

You can intercepts events by subclassing the widgets and overriding their event handlers

```python
class CustomButton(QButton):
    def keyPressEvent(self,event):
        print(event)
        super(CustomButton,self).keyPressEvent(event)
```

However imagine now you want to intercept such events on hundreds of buttons.
Subclassing each button and intercepting events like above becomes tedious.

# Signals
Instead of intercepting raw events, ```signal```s allow you 
to listen to a specific notification of things happening.

The handlers, regular python functions, connected to ```signals```
are called ```slots```
```python
button_action.triggered.connect(<my handler>)
```
