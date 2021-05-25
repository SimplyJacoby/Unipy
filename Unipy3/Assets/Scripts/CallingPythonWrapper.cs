using UnityEngine;

public class CallingPythonWrapper : MonoBehaviour
{
    public CallingPython callingPython = new CallingPython();
    public void Run()
    {
        callingPython.RunCallingPython();
    }
}
