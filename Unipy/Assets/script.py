import UnityEngine

# Getting the values from the two UI Text objects called num1 and num2
num1 = UnityEngine.GameObject.Find("num1").GetComponent("UnityEngine.UI.Text").text
num2 = UnityEngine.GameObject.Find("num2").GetComponent("UnityEngine.UI.Text").text
UnityEngine.Debug.Log("Static numbers in Unity Text objects: " + num1 + ", " + num2)

# Getting the font of the UI Text object called num1
font = UnityEngine.GameObject.Find("num1").GetComponent("UnityEngine.UI.Text").font
UnityEngine.Debug.Log("Font of Unity Text object: " + str(font))

# Setting the value of the UI Text object called num3 as the sum of num1 and num2
UnityEngine.GameObject.Find("num3").GetComponent("UnityEngine.UI.Text").text = str(int(num1) + int(num2))

# Getting the value of the variable called num_in_c from the calling C# script
num_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").num_in_c
UnityEngine.Debug.Log("Global int variable in C# script: " + str(num_in_c))

# Getting the value of the String variable called string_in_c from the calling C# script
string_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").string_in_c
UnityEngine.Debug.Log("Global String in C# script: " + string_in_c)

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
UnityEngine.Debug.Log("Global array variable in C# script: " + str(list_in_python))

# Setting a value in array_in_c
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").array_in_c[0] = 5

# Adding two values to array_in_c
list_in_python.append(4)
list_in_python.append(5)
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").new_length_array_in_c = len(list_in_python)
for i in range(0, len(list_in_python)):
    UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").new_arraylist_in_c.Add(list_in_python[i])

# Getting the values from the two UI InputFields called inputnum1 and inputnum2
num1 = UnityEngine.GameObject.Find("inputnum1").GetComponent("UnityEngine.UI.InputField").text
num2 = UnityEngine.GameObject.Find("inputnum2").GetComponent("UnityEngine.UI.InputField").text

UnityEngine.Debug.Log("Input numbers in Unity InputField objects: " + num1 + ", " + num2)

# Setting the value of the UI Text object called inputnum3 as the sum of num1 and num2
UnityEngine.GameObject.Find("inputnum3").GetComponent("UnityEngine.UI.Text").text = str(int(num1) + int(num2))