using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using Habrador_Computational_Geometry;

public class ConvexHull : MonoBehaviour
{

    public GameObject convexx ;

    void buildMesh(Vector3[] vertices, int[] triangles, GameObject meshToBuild)
    {
        Mesh newMesh = new Mesh();
        newMesh.Clear();
        newMesh.vertices = vertices;
        newMesh.triangles = triangles;
        newMesh.RecalculateNormals();

        meshToBuild.GetComponent<MeshFilter>().sharedMesh = newMesh;
    }

    
    // Start is called before the first frame update
    void Start()
    {
         string path = "ConvexHullVertices.txt";
         readTextFile(path);
        /////////////////////////////////////////////
            Texture2D source = GetComponent<SpriteRenderer>().sprite.texture;
            byte[] pix = source.GetRawTextureData();
            Texture2D readableText =new Texture2D(source.width,source.height,source.format,false);
            readableText.LoadRawTextureData(pix);
            readableText.Apply();


    }
    List <Vector3> vec = new List<Vector3>(); 
    void readTextFile(string file_path)
        {
            StreamReader inp_stm = new StreamReader(file_path);
            
            while(!inp_stm.EndOfStream)
            {
                string inp_ln = inp_stm.ReadLine( );
                Debug.Log(inp_ln);
                string [] arr = inp_ln.Replace("[","").Replace("]","").Replace(" ","").Split(',');
                Vector3 pos = new Vector3(float.Parse(arr[0]),float.Parse(arr[1]),float.Parse(arr[2])); 

                      GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere); 
                      sphere.transform.position = pos;

                      sphere.GetComponent<Renderer>().material.color = new Color(pos[0],pos[1],pos[2]);
                      
                      sphere.transform.localScale= new Vector3(0.1f,0.1f,0.1f);
                      vec.Add(pos);
            }

            HalfEdgeData3 hulll =  IterativeHullAlgorithm3D.GenerateConvexHull(vectorListToHashSet(vec), true);
            MyMesh convexMesh = hulll.ConvertToMyMesh("MyConvex", MyMesh.MeshStyle.HardEdges);
            Mesh convexHull = convexMesh.ConvertToUnityMesh(false, convexMesh.meshName);
            buildMesh(convexHull.vertices,convexHull.triangles,convexx);
           
           
            for(int i =0;i<vec.Count;i++)
            {
                for(int j =0;j<vec.Count;j++)
                {     
                  Debug.DrawLine(vec[i], vec[j], new Color(vec[i].x,vec[i].y,vec[i].z), 0.04f);
                }
            }
             
             inp_stm.Close( );  
                   
                   
        }
        void Update()
        {
            for(int i =0;i<vec.Count;i++)
            {
                    for(int j =0;j<vec.Count;j++)
                    {     
                    Debug.DrawLine(vec[i], vec[j], new Color(vec[i].x,vec[i].y,vec[i].z), 0.04f);
                    }
            }
        }
        public HashSet<MyVector3> vectorListToHashSet(List<Vector3> list)
        {
            HashSet<MyVector3> hashSet = new HashSet<MyVector3>();

            for (int i = 0; i < list.Count; i++)
            {
                hashSet.Add(new MyVector3(list[i].x, list[i].y, list[i].z));
            }

            return hashSet;
        }

   
}
