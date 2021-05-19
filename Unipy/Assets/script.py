# import UnityEngine
# UnityEngine.Debug.Log("Hello world")

import UnityEngine
import UnityEngine.UI

num1 = UnityEngine.GameObject.Find("num1").GetComponent(UnityEngine.UI.Text).text
num2 = UnityEngine.GameObject.Find("num2").GetComponent(UnityEngine.UI.Text).text

UnityEngine.Debug.Log(num1)
UnityEngine.Debug.Log(num2)

UnityEngine.GameObject.Find("num3").GetComponent(UnityEngine.UI.Text).text = str(int(num1) + int(num2))