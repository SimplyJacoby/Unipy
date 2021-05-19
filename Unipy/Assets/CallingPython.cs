using UnityEditor;
using UnityEditor.Scripting.Python;
using UnityEngine;
using System;
using System.IO;
using System.Text;

public class CallingPython
{
    [MenuItem("Python/CallingPython")]
    static void RunCallingPython()
    {
        PythonRunner.RunFile($"{Application.dataPath}/script.py");
    }
}


