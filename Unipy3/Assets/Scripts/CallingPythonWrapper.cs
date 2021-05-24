using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CallingPythonWrapper : MonoBehaviour
{
    public CallingPython callingPython = new CallingPython();
    public void Run()
    {
        callingPython.RunCallingPython();
    }
}
