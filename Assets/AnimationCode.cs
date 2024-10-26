using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;
using System.Threading;

public class AnimationCode : MonoBehaviour
{
    public GameObject[] Body;
    private List<string> lines;
    private int counter = 0;

    void Start()
    {
        lines = System.IO.File.ReadLines("Assets/pose_coordinates.txt").ToList();
    }

    void Update()
    {
        string[] points = lines[counter].Split(',');

        for (int i = 0; i < Body.Length; i++)
        {
            float x = float.Parse(points[0 + (i * 3)]) / 100;
            float y = -float.Parse(points[1 + (i * 3)]) / 100; // Invert the y value
            float z = float.Parse(points[2 + (i * 3)]) / 100;
            Body[i].transform.localPosition = new Vector3(x, y, z);
        }

        counter++;
        if (counter == lines.Count)
        {
            counter = 0;
        }
        Thread.Sleep(30);
        // Removed Thread.Sleep(30) as it's not suitable for Unity's main thread
    }
}
