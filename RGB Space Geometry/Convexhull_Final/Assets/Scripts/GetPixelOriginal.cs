using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class GetPixelOriginal : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        

        /////////////////////////////////////////////
        ExtractImage();
    }

    void ExtractImage() 
    {
        StreamWriter writer = new StreamWriter(".txt");
        Texture2D source = GetComponent<SpriteRenderer>().sprite.texture;
        byte[] pix = source.GetRawTextureData();
        Texture2D readableText =new Texture2D(source.width,source.height,source.format,false);
        readableText.LoadRawTextureData(pix);
        readableText.Apply();
        Debug.Log(readableText.width + "," +  readableText.height);
        for(int w=410;w<readableText.width;w++)
        {
            for(int h=380;h<readableText.height;h++)
            {
                Color clr = readableText.GetPixel(w,h);
                writer.WriteLine(clr.r + "," + clr.g + "," + clr.b);
                Color32 Pixel = clr;

                Debug.Log($"Color at {w}, {h} is: {clr.r}, {clr.g}, {clr.b}");
                Debug.Log($"Color at {w}, {h} is: {Pixel.r}, {Pixel.g}, {Pixel.b}");
               
            }
        }
    }


    // Update is called once per frame
    void Update()
    {
        
    }
}
