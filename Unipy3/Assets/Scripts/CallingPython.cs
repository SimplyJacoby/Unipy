using System.Collections;
using UnityEngine;
using Python.Runtime;
using UnityEditor.Scripting.Python;
using System;
using UnityEngine.UI;

public class CallingPython
{
    public int num_in_c = 3;
    public int[] array_in_c = new int[] { 1, 2, 3 };
    public int length_array_in_c = 0;
    public String string_in_c = "hello";
    public ArrayList new_arraylist_in_c = new ArrayList();

    public void RunCallingPython()
    {
        PythonRunner.EnsureInitialized();
        using (Py.GIL())
        {
            try
            {
                length_array_in_c = array_in_c.Length;
                PythonRunner.RunFile($"{Application.dataPath}/Python/script.py");
                GameObject.Find("newValues").GetComponent<Text>().text += "\nnum_in_c: " + num_in_c.ToString();
                GameObject.Find("newValues").GetComponent<Text>().text += "\nstring_in_c: " + string_in_c;
                array_in_c = (int[])new_arraylist_in_c.ToArray(typeof(int));
                GameObject.Find("newValues").GetComponent<Text>().text += "\narray_in_c: [" + string.Join(", ", array_in_c) + " ]";
            }
            catch (PythonException e)
            {
                Debug.LogException(e);
            }
        }
    }
}

