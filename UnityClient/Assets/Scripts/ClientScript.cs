using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class ClientScript : MonoBehaviour
{
    public void Run()
    {
        string message = ConnectAndExecute();
        GameObject.Find("output").GetComponent<Text>().text += "\nmessage: " + message;
    }

    private static string ConnectAndExecute()
    {
        //IPHostEntry host = Dns.GetHostEntry(Dns.GetHostName());
        IPHostEntry host = Dns.GetHostEntry("54.92.132.97");
        IPEndPoint ipe = new IPEndPoint(host.AddressList[0], 7734);
        Socket s = new Socket(ipe.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
        s.Connect(ipe);
        if (!s.Connected)
        {
            throw new Exception("could not connect to server");
        }

        string message = "Hello from client";
        s.Send(Encoding.ASCII.GetBytes(message));

        byte[] receivedMessage = new byte[4096];
        int receivedBytes = s.Receive(receivedMessage);
        string receivedString = Encoding.ASCII.GetString(receivedMessage, 0, receivedBytes);

        s.Shutdown(SocketShutdown.Both);
        s.Close();
        return receivedString;
    }
}
