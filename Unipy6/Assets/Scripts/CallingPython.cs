using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CallingPython : MonoBehaviour
{
    public void Run()
    {
        using (Py.GIL())
        {
            using (PyScope scope = Py.CreateScope())
            {

            }
        }
    }
}
