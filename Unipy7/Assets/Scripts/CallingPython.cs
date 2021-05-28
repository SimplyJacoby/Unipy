using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Python.Runtime;
using System;
using System.IO;
using UnityEngine.UI;

public class CallingPython : MonoBehaviour
{
    void Start()
    {
        Runtime.PythonDLL = Application.dataPath + "/StreamingAssets/python-3.9.5-embed-amd64/python39.dll";
        PythonEngine.Initialize(mode: ShutdownMode.Soft);
    }

    public void OnApplicationQuit()
    {
        if (PythonEngine.IsInitialized)
        {
            PythonEngine.Shutdown();
        }
    }

    public void Run()
    {
        using (Py.GIL())
        {
            dynamic sys = PyModule.Import("sys");
            sys.path.append(@"C:/Users/Jacob Bream/Documents/Biomojo/Unipy/Unipy7/Assets/Python");

            dynamic scope = Py.Import("script");
            String message = scope.hello("Jacob");
            int[] arr = scope.getArrayOfSize(5);
            int arr_sum = scope.getSumOfArray(arr);
            int exp = scope.exponent(2, 3);
            float sin = scope.sin(5);
            float integral = scope.integrate(-1, 1);
            dynamic fido = scope.Dog("Fido");
            String walk = fido.walk(5);
            GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + message;
            GameObject.Find("output").GetComponent<Text>().text += "\narray: [" + string.Join(", ", arr) + "]";
            GameObject.Find("output").GetComponent<Text>().text += "\nsum of array: " + arr_sum.ToString();
            GameObject.Find("output").GetComponent<Text>().text += "\nexponent: " + exp.ToString();
            GameObject.Find("output").GetComponent<Text>().text += "\nsin: " + sin.ToString();
            GameObject.Find("output").GetComponent<Text>().text += "\nintegral: " + integral.ToString();
            GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + walk;
        }
    }
}
