using UnityEditor;
using UnityEditor.Scripting.Python;
using UnityEngine;
using System;


public class CallingPython : MonoBehaviour
{
    public int num_in_c = 3;
    public int[] array_in_c = new int[] { 1, 2, 3 };
    public String string_in_c = "hello";

    [MenuItem("Python/CallingPython")]
    public static void RunCallingPython() 
    {
        PythonRunner.RunFile($"{Application.dataPath}/script.py");
    }

    public void Run()
    {
        RunCallingPython();
        Debug.Log("Updated String in C#");
        Debug.Log(string_in_c);
    }
}


