using System.Collections;
using System.Collections.Generic;
using System.IO;
using UnityEngine;
using System;
using System.Linq;
using UnityEngine.UI;

public class CentroidColor : MonoBehaviour
{
    // Start is called before the first frame update
    public float

            x,
            y,
            z;

    StreamWriter writer;
    public RawImage kImage;
    bool isReady = false;

    void Start()
    {

        GetComponent<Renderer>().material.color = new Color32(byte.Parse(Convert.ToInt32(x).ToString()), byte.Parse(Convert.ToInt32(y).ToString()),
            byte.Parse(Convert.ToInt32(z).ToString()), 255);
        string path = "_Direction.txt";
        readTextFile(path);
        writer = new StreamWriter("_Hitting.txt");



 
    }

    // Update is called once per frame
    void Update()
    {

        if (Input.GetKeyUp(KeyCode.M))
        {
            isReady = true;

        }
        if (newCount > ct)
        {
            DetectKey();
        }


    }

    public void SetImage()
    {
        List<Color32> kImageVals = ReadKImageFile();


        Texture2D copyTexture = new Texture2D(512, 512);


        for (int r = 0, i = 0; r < copyTexture.height; r++)
        {
            for (int c = 0; c < copyTexture.width; c++)
            {
                Color32 clr = kImageVals[i];
                copyTexture.SetPixel(c, r, clr);
                i++;
            }
        }

        copyTexture.Apply();
        kImage.texture = copyTexture;


    }

    List<Vector3> rayyy = new List<Vector3>();

    void readTextFile(string file_path)
    {
        StreamReader inp_stm = new StreamReader(file_path);
        List<int> x = new List<int>();
        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();

            string[] arr =
                inp_ln
                    .Replace("[", "")
                    .Replace("]", "")
                    .Replace(" ", "")
                    .Split(',');

            
            Vector3 pos = new Vector3(float.Parse(arr[0]), float.Parse(arr[1]), float.Parse(arr[2]));
            rayyy.Add(pos);

            x.Add(1);
        }


        inp_stm.Close();
        return;
    }

    int ct = 0;

    public void DetectKey()
    {

        if (rayyy != null && ct < rayyy.Count && isReady == true)
        {
            Raycasttt();


            Vector3 Direc = ((rayyy[ct] * 10) - transform.position).normalized;
            Debug.DrawRay(transform.position + Direc * 100, -Direc * 10000, gameObject.GetComponent<Renderer>().material.color);

        }
        else if (rayyy != null && ct >= rayyy.Count && isReady)
        {
            Debug.Log("Finished raycasting");
            writer.Close();
            isReady = false;
        }

    }

    int newCount = 1;
    void Raycasttt()
    {
        RaycastHit[] hits;
        Vector3 Direc = ((rayyy[ct] * 10) - transform.position).normalized;

        hits =
            Physics
                .RaycastAll(transform.position + Direc * 100000,
                -Direc,
                Mathf.Infinity);
        ct = newCount;

        if (hits.Length > 0)
        {
            foreach (var hit in hits)
            {
                if (hit.collider != null)
                {
                    

                    if (!hit.collider.gameObject.name.Contains("Centroid"))
                    {
                        

                        WriteString(hit.point.x +
                        "," +
                        hit.point.y +
                        "," +
                        hit.point.z);

                        newCount++;
                        break;

                    }
                }
            }

            if (ct == newCount)
            {
                ct = newCount - 1;
                float oldX = rayyy[ct].x;
                rayyy[ct] = new Vector3(oldX + 0.00001f, rayyy[ct].y, rayyy[ct].z);
                Debug.Log($"Old rayn x = {oldX}, new x: {rayyy[ct].x}");
            }


        }
    }

    void WriteString(string str)
    {
        writer.WriteLine(str);

    }



    void NewRaycast()
    {
        Vector3 Cnt = transform.position;

        if (Input.GetKeyDown(KeyCode.UpArrow))
        {
            if (ct < rayyy.Count - 1)
            {
                ct++;
            }
            else
            {
                ct = 0;
            }
        }

        Vector3 Direc = (rayyy[ct] - transform.position).normalized;
        Ray ray1 = new Ray(Cnt, Direc);

        Debug.DrawRay(Cnt, Direc, Color.red, duration: 2f);

        RaycastHit hit;
        if (Physics.Raycast(ray1, out hit))
        {
            print("yes");
            print(hit.collider.name);
        }
    }



    public void CreateK_Image()
    {
        writer = new StreamWriter("_KImage.txt");
        Dictionary<Color32, float> pixelDictionary = new Dictionary<Color32, float>();
        List<Color32> pointDub = readfilePointDub();
        List<float> MapK = readfileKMap();
        List<Color32> Original = readfileOriginal();
        List<float> NewImage = new List<float>();

        for (int i = 0; i < pointDub.Count; i++)
        {
            pixelDictionary.Add(pointDub[i], MapK[i]);
        }

        for (int i = 0; i < Original.Count; i++)
        {
            float value = pixelDictionary.Where(pixel => pixel.Key.r == Original[i].r &&
                                                         pixel.Key.g == Original[i].g &&
                                                         pixel.Key.b == Original[i].b).FirstOrDefault().Value;
            NewImage.Add(value);
            WriteString(value.ToString());
        }

        Debug.Log("finished writing k");
        writer.Close();

    }

    List<Color32> ReadKImageFile()
    {
        string path2 = "_KImage.txt";
        List<Color32> kImageValues = new List<Color32>();
        StreamReader inp_stm = new StreamReader(path2);

        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();
            string[] arr = inp_ln.Replace(" ", "").Replace("(", "").Replace(")", "").Split(",");

            float floatValue = float.Parse(arr[0]);
            if (floatValue > 255)
            {
                Debug.Log("found " + floatValue);
                floatValue -= 255;
                arr[0] = floatValue.ToString();
            }
            byte val = byte.Parse(Convert.ToInt32(float.Parse(arr[0])).ToString());
            Color32 clr = new Color32(val, val, val, 255);
            kImageValues.Add(clr);
        }

        inp_stm.Close();
        return kImageValues;
    }

    List<Color32> readfileOriginal()
    {
        string path2 = ".txt";
        List<Color32> Original = new List<Color32>();
        StreamReader inp_stm = new StreamReader(path2);
        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();
            string[] arr = inp_ln.Replace(" ", "").Replace("(", "").Replace(")", "").Split(',');
            // Debug.Log(inp_ln);
            Color32 valueOrg = new Color32(byte.Parse(arr[0]), byte.Parse(arr[1]), byte.Parse(arr[2]), 255);
            Original.Add(valueOrg);
        }
        inp_stm.Close();
        return Original;
    }


    List<Color32> readfilePointDub()
    {
        string path2 = "_RemovedDuplicatePixels.txt";
        List<Color32> pointDub = new List<Color32>();
        StreamReader inp_stm = new StreamReader(path2);
        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();
            string[] arr = inp_ln.Replace(" ", "").Split(',');
            // Debug.Log(inp_ln);
            Color32 valuePointDub = new Color32(byte.Parse(Convert.ToInt32(float.Parse(arr[0])).ToString()),
                byte.Parse(Convert.ToInt32(float.Parse(arr[1])).ToString()), byte.Parse(Convert.ToInt32(float.Parse(arr[2])).ToString()), 255);
            pointDub.Add(valuePointDub);
        }
        inp_stm.Close();
        return pointDub;
    }

    List<float> readfileKMap()
    {
        string path2 = "_Mapp_K.txt";
        List<float> MapK = new List<float>();
        StreamReader inp_stm = new StreamReader(path2);
        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();
            string[] arr = inp_ln.Replace(" ", "").Split(',');
            //  Debug.Log(inp_ln);
            MapK.Add(float.Parse(arr[0]));
        }
        inp_stm.Close();
        return MapK;
    }
}


