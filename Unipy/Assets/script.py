import UnityEngine

# Getting the values from the two UI Text objects called num1 and num2
num1 = UnityEngine.GameObject.Find("num1").GetComponent("UnityEngine.UI.Text").text
num2 = UnityEngine.GameObject.Find("num2").GetComponent("UnityEngine.UI.Text").text

# Getting the font of the UI Text object called num1
font = UnityEngine.GameObject.Find("num1").GetComponent("UnityEngine.UI.Text").font

UnityEngine.Debug.Log("Static numbers in Unity Text objects")
UnityEngine.Debug.Log(num1)
UnityEngine.Debug.Log(num2)
UnityEngine.Debug.Log("Font of Unity Text object")
UnityEngine.Debug.Log(font)

# Setting the value of the UI Text object called num3 as the sum of num1 and num2
UnityEngine.GameObject.Find("num3").GetComponent("UnityEngine.UI.Text").text = str(int(num1) + int(num2))

# Getting the value of the variable called num_in_c from the calling C# script
num_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").num_in_c

#Getting the array called arr_in_c from the calling C# script
array_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").array_in_c

# Getting the value of the String variable called string_in_c from the calling C# script
string_in_c = UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").string_in_c

UnityEngine.Debug.Log("Global String in C# script")
UnityEngine.Debug.Log(string_in_c)

# Setting the value of the String variable called string_in_c in the C# script
UnityEngine.GameObject.Find("ScriptHolder").GetComponent("CallingPython").string_in_c = "new string"

UnityEngine.Debug.Log("Global int variable in C# script")
UnityEngine.Debug.Log(num_in_c)
UnityEngine.Debug.Log("Global array variable in C# script")
UnityEngine.Debug.Log(array_in_c[0])
UnityEngine.Debug.Log(array_in_c[1])
UnityEngine.Debug.Log(array_in_c[2])

# Getting the values from the two UI InputFields called inputnum1 and inputnum2
num1 = UnityEngine.GameObject.Find("inputnum1").GetComponent("UnityEngine.UI.InputField").text
num2 = UnityEngine.GameObject.Find("inputnum2").GetComponent("UnityEngine.UI.InputField").text

UnityEngine.Debug.Log("Input numbers in Unity InputField objects")
UnityEngine.Debug.Log(num1)
UnityEngine.Debug.Log(num2)

# Setting the value of the UI Text object called inputnum3 as the sum of num1 and num2
UnityEngine.GameObject.Find("inputnum3").GetComponent("UnityEngine.UI.Text").text = str(int(num1) + int(num2))