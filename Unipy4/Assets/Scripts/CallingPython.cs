using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using IronPython.Hosting;
using System;
using UnityEngine.UI;

public class CallingPython : MonoBehaviour
{
    public void Run()
    {
        var engine = Python.CreateEngine();

        dynamic py = engine.ExecuteFile("C:/Users/Jacob Bream/Documents/Biomojo/Unipy/Unipy4/Assets/Python/script.py");

        String message = py.hello("Jacob");
        int[] arr = py.arr;
        dynamic fido = py.Dog("Fido");
        String walk = fido.walk(5);

        GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + message;
        GameObject.Find("output").GetComponent<Text>().text += "\narray: [" + string.Join(", ", arr) + "]";
        GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + walk;
    }
}
