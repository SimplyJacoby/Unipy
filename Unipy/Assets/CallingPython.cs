using UnityEditor;
using UnityEditor.Scripting.Python;
using UnityEngine;
using System;
using System.Collections;


public class CallingPython : MonoBehaviour
{
    public int num_in_c = 3;
    public int[] array_in_c = new int[] { 1, 2, 3 };
    public int length_array_in_c = 0;
    public String string_in_c = "hello";

    public ArrayList new_arraylist_in_c = new ArrayList();

    [MenuItem("Python/CallingPython")]
    public static void RunCallingPython() 
    {
        PythonRunner.RunFile($"{Application.dataPath}/script.py");
    }

    public void Run()
    {
        length_array_in_c = array_in_c.Length;
        RunCallingPython();
        Debug.Log("Updated String in C#: " + string_in_c);
        Debug.Log("Global array variable in C# script, new index 0: " + array_in_c[0]);
        array_in_c = (int[])new_arraylist_in_c.ToArray(typeof(int));
        Debug.Log("Updated array in C# script: " + string.Join(", ", array_in_c));
    }
}


