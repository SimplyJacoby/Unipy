using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using IronPython.Hosting;
using System;
using UnityEngine.UI;
using Microsoft.Scripting.Hosting;

public class CallingPython : MonoBehaviour
{
    public void Run()
    {
        ScriptEngine engine = Python.CreateEngine();

        ICollection<string> searchPaths = engine.GetSearchPaths();
        searchPaths.Add(@"C:/Users/Jacob Bream/Documents/Biomojo/Unipy/Unipy5/Assets/Plugins/IronPython.3.4.0-alpha1/Lib");
        searchPaths.Add(@"C:/Users/Jacob Bream/Documents/Biomojo/Unipy/Unipy5/Assets/Plugins/IronPython.3.4.0-alpha1/Lib/site-packages");
        engine.SetSearchPaths(searchPaths);

        dynamic py = engine.ExecuteFile("C:/Users/Jacob Bream/Documents/Biomojo/Unipy/Unipy5/Assets/Python/script.py");

        String message = py.hello("Jacob");
        int[] arr = py.arr;
        dynamic fido = py.Dog("Fido");
        String walk = fido.walk(5);

        GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + message;
        GameObject.Find("output").GetComponent<Text>().text += "\narray: [" + string.Join(", ", arr) + "]";
        GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + walk;
    }
}
