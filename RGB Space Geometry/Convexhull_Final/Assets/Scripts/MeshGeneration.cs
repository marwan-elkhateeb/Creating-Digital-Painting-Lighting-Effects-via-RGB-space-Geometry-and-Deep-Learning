using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using Habrador_Computational_Geometry;

[RequireComponent(typeof(MeshFilter))]

public class MeshGeneration : MonoBehaviour
{
    Mesh mesh;
    Vector3[] vertices;
    int[] triangles;
    // Start is called before the first frame update

    void Start()
    {
        mesh = new Mesh {
            name = "Procedural Mesh"
        };
        GetComponent<MeshFilter>().mesh = mesh;
        string patht = "Simplices(Triangles).txt";
        string pathv = "ConvexHullVertices.txt";
        string pathabc = "simplicesABC.txt";
        TrianglesRead(patht);
        vertecesREAD(pathv);
        TriangleABCRead(pathabc);
        CreateShape();
        UpdateMesh();
    }
public class face{
    // points of faces (3 points)
    public Vector3 points = new Vector3();

    public void set_points(float x, float y, float z)
    {
        points.x = x;
        points.y = y;
        points.z = z;

    }
}



List<Vector3> abcvec = new List<Vector3>();
void TriangleABCRead(string file_path)
    {
            StreamReader inp_stm = new StreamReader(file_path);
            int Count= 0;
            while(!inp_stm.EndOfStream)
            {
                string inp_ln = inp_stm.ReadLine( );
                string [] arr = inp_ln.Replace("a","").Replace("b","").Replace("c","").Replace("=","").Replace(" ","").Split(',');
                Vector3 pos = new Vector3(float.Parse(arr[0]),float.Parse(arr[1]),float.Parse(arr[2])); 
                abcvec.Add(pos);
                compareabc(pos, vec);
            }

            for(int i =0; i<newfaces.Count ; i++)
            {
                print(newfaces[i]);
            }
            inp_stm.Close( );         
    }

List<int> newfaces = new List<int>();
void compareabc(Vector3 abc, List<Vector3> vec)
{
    for(int i =0 ; i<vec.Count ; i++)
    {
        if(abc.x == vec[i].x)
        {
            if(abc.y == vec[i].y)
            {
                if(abc.z == vec[i].z)
                {
                   newfaces.Add(i);
                }
            }
        }
    }
}


    // Triangles
    List<face> faces = new List<face>(); //triangles
    List <Vector3> vec = new List<Vector3>();   //vectors
    void TrianglesRead(string file_path)
    {
            StreamReader inp_stm = new StreamReader(file_path);
            int Count= 0;
            face pnn = new face();
            while(!inp_stm.EndOfStream)
            {
                string inp_ln = inp_stm.ReadLine( );
                string [] arr = inp_ln.Replace("[","").Replace("]","").Replace(" ","").Split(',');
                Vector3 pos = new Vector3(int.Parse(arr[0]),int.Parse(arr[1]),int.Parse(arr[2])); 

                
                face pnnface = new face();
                pnnface.set_points(pos.x, pos.y, pos.z);

                faces.Add(pnnface);
            }
            

             
            inp_stm.Close( );         
    }



 void vertecesREAD(string file_path)
        {
            StreamReader inp_stm = new StreamReader(file_path);
            while(!inp_stm.EndOfStream)
            {
                string inp_ln = inp_stm.ReadLine( );
                string [] arr = inp_ln.Replace("[","").Replace("]","").Replace(" ","").Split(',');
                Vector3 pos = new Vector3(float.Parse(arr[0]),float.Parse(arr[1]),float.Parse(arr[2])); 

                      vec.Add(pos);
            }


    
             inp_stm.Close( );  
                   
                   
        }
   List<int> TRII = new List<int>();
   List<Vector3> VECC = new List<Vector3>();
    void CreateShape()
    {

          for(int i =0; i<vec.Count ; i++)
             {
                 VECC.Add(vec[i]);
             }

        
          for(int i =0; i<newfaces.Count ; i++)
             {
                TRII.Add(newfaces[i]);
             }
        print(">>>>>>>>>>>>>>>>>>>>>>>>>"+VECC.Count);
        print(">>>>>>>>>>>>>>>>>>>>>>>>>"+TRII.Count);
    }
    void UpdateMesh()
    {
        mesh.Clear();

        mesh.vertices = VECC.ToArray();
        mesh.triangles = TRII.ToArray();

        mesh.RecalculateNormals();
    }
    
    void Update()
    {
         UpdateMesh();
    }
}

    

