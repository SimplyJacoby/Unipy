import UnityEngine

# Getting the value of the variable called num_in_c from the calling C# script
num_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").num_in_c
UnityEngine.GameObject.Find("oldValues").GetComponent("UnityEngine.UI.Text").text += "\nnum_in_c: " + str(num_in_c)

# Setting the value of the int variable called num_in_c in the C# script
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").num_in_c = 4

# Getting the value of the String variable called string_in_c from the calling C# script
string_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").string_in_c
UnityEngine.GameObject.Find("oldValues").GetComponent("UnityEngine.UI.Text").text += "\nstring_in_c: " + string_in_c

# Setting the value of the String variable called string_in_c in the C# script
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").string_in_c = "new string"

# Getting the array called arr_in_c from the calling C# script. Since python doesn't have strict arrays,
# it has Lists, we must iterate through the array to convert it to a List. To do this, we need to know the
# length of the array, which isn't easy within Python, so we store the length in a C# variable which we can
# access in Python.
array_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").array_in_c
length_array_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").length_array_in_c
list_in_python = []
for i in range(0, length_array_in_c):
    list_in_python.append(array_in_c[i])
UnityEngine.GameObject.Find("oldValues").GetComponent("UnityEngine.UI.Text").text += "\narray_in_c: " + str(list_in_python)

# Setting a value in array_in_c. Set in python to avoid overwriting by later converting in the C# script
list_in_python[0] = 5
# If you don't plan on adding or deleting values which would require conversion in C#. you can set by indexing like this:
# UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").array_in_c[0] = 5

# Adding two values to array_in_c
list_in_python.append(4)
list_in_python.append(5)
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").new_length_array_in_c = len(list_in_python)
for i in range(0, len(list_in_python)):
    UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").new_arraylist_in_c.Add(list_in_python[i])

# Getting the values from the two UI InputFields called inputnum1 and inputnum2
num1 = UnityEngine.GameObject.Find("num1").GetComponent("UnityEngine.UI.InputField").text
num2 = UnityEngine.GameObject.Find("num2").GetComponent("UnityEngine.UI.InputField").text

UnityEngine.Debug.Log("Input numbers in Unity InputField objects: " + num1 + ", " + num2)

# Setting the value of the UI Text object called inputnum3 as the sum of num1 and num2
UnityEngine.GameObject.Find("answer").GetComponent("UnityEngine.UI.Text").text = str(int(num1) + int(num2))