using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System;
using System.IO;

public class Sphere : MonoBehaviour
{
    List<Color> RGB = new List<Color>();
    void Start()
    {

        string path = "text.txt";
        readTextFile(path);
        StreamWriter writer = new StreamWriter(".txt");

        /////////////////////////////////////////////
        Texture2D source = GetComponent<SpriteRenderer>().sprite.texture;
        byte[] pix = source.GetRawTextureData();
        Texture2D readableText =new Texture2D(source.width,source.height,source.format,false);
        readableText.LoadRawTextureData(pix);
        readableText.Apply();
        for(int w=0;w<readableText.width;w++)
        {
            for(int h=0;h<readableText.height;h++)
            {
             //   print(">>" + readableText.GetPixel(w,h));
                Color clr = readableText.GetPixel(w,h);
                if(isDub(clr))
                {
                    GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
                    sphere.transform.position = new Vector3(clr.r, clr.g, clr.b);
                    //WriteString(clr.r+","+clr.g+","+clr.b);
                    writer.WriteLine(clr.r + "," + clr.g + "," + clr.b);
                    //  sphere.GetComponent<Renderer>().SetColor(clr);
                    sphere.GetComponent<Renderer>().material.color = clr;
                    sphere.transform.localScale= new Vector3(0.02f,0.02f,0.02f);
                    RGB.Add(clr);
                }

            }
        }
        Debug.Log(RGB.Count);
        
    }
    bool isDub(Color clr)
    {
         for(int i =0 ;i<RGB.Count;i++)
        {
            if(RGB[i]==clr)
            {
                return false;
            }
        }
      return true;  
    }
    
        void readTextFile(string file_path)
        {
            StreamReader inp_stm = new StreamReader(file_path);

            while(!inp_stm.EndOfStream)
            {
                string inp_ln = inp_stm.ReadLine( );
                Debug.Log(inp_ln);
            }

             inp_stm.Close( );  
        }


}
