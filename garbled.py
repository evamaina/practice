garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]
print message

"""The string above is garbled in two ways:Our message is backwards.
The letter we want is every other letter.Use list slicing to extract
the message and save it to a variable called message."""

"""It's important to remember that lists are mutable (changeable) in Python,
 but strings aren't; when you slice a string, you get back a new string"""