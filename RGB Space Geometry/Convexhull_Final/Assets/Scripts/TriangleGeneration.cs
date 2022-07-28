using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;

public class TriangleGeneration : MonoBehaviour
{
    Vector3[] verticesArr;
    int[] trianglesArr;
    Vector3[] normals;
    Mesh mesh;
    public GameObject meshObject;
    public GameObject centroidObject;


    public GameObject S1;
    // Start is called before the first frame update
    void Start()
    {
        //GetComponent<Renderer>().material.color = new Color(x,y,z);
        string path1 = ".txt";
        readTextFile1(path1);


        string path = "simplicesABC.txt";
        readTextFile(path);

        mesh = new Mesh();
        //GetComponent<MeshFilter>().mesh = mesh;

    }

    List <Vector3> rayyy = new List<Vector3>();  
    void readTextFile1(string file_path)
    {
       // print("3ash");
        StreamReader inp_stm = new StreamReader(file_path);
        List<int> x = new List<int>();
        while(!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine( );

            string [] arr = inp_ln.Replace("[","").Replace("]","").Replace(" ", "").Replace("\n", " ").Split(',');
            //print(arr.Length);
            Vector3 pos = new Vector3(float.Parse(arr[0]),float.Parse(arr[1]),float.Parse(arr[2])); 
            rayyy.Add(pos);
            x.Add(1);
            
        }
        //print(" >>> " + x.Count);
        inp_stm.Close( );
        return;
    }



    List<face> faces = new List<face>();
    List<Vector3> vec = new List<Vector3>();
     void readTextFile(string file_path)
    {
        StreamReader inp_stm = new StreamReader(file_path);
        int Count = 0;
        face pnn = new face();
        while (!inp_stm.EndOfStream)
        {
            string inp_ln = inp_stm.ReadLine();
            //                Debug.Log(inp_ln);
            string[] arr = inp_ln.Replace("a", "").Replace("b", "").Replace("c", "").Replace(" ", "").Replace("=", "").Split(',');
            Vector3 pos = new Vector3(float.Parse(arr[0]), float.Parse(arr[1]), float.Parse(arr[2]));
            vec.Add(pos);
            pnn.points.Add(pos);
            Count++;
            if (Count == 3)
            {
                faces.Add(pnn);
                pnn = new face();
                GenerateMesh();
                Count = 0;
            }
            
        }
       
        inp_stm.Close();
    }

    void Create()
    {
        verticesArr = new Vector3[]
        {
            vec[vec.Count - 1],
            vec[vec.Count - 2],
            vec[vec.Count - 3],
            Vector3.zero 


        };

        trianglesArr = new int[]
        {
            0,1,2
            //2,1,0
        };

    }

    void UpdateMesh()
    {
        mesh = new Mesh();
        mesh.Clear();
        mesh.vertices = verticesArr;
        mesh.triangles = trianglesArr;

        
        mesh.RecalculateNormals();
        normals = mesh.normals;
    }

    void GenerateMesh()
    {
        GameObject newMeshObject = Instantiate(meshObject, meshObject.transform.position, Quaternion.identity);
        newMeshObject.name = "triangle number " + faces.Count ;

        

        newMeshObject.AddComponent<MeshCollider>().convex = true;
        newMeshObject.GetComponent<MeshCollider>().isTrigger = false;
        

        Create();
        UpdateMesh();
        newMeshObject.GetComponent<MeshFilter>().mesh = mesh;

    }
    
    // Update is called once per frame
    void Update()
    {
            float xc = (verticesArr[0].x + verticesArr[1].x + verticesArr[2].x) / 3;
            float yc = (verticesArr[0].y + verticesArr[1].y + verticesArr[2].y) / 3;
            float zc = (verticesArr[0].z + verticesArr[1].z + verticesArr[2].z) / 3;

            Vector3 Cnt = new Vector3(xc,yc, zc);
            Ray ray1 = new Ray (S1.transform.position , Cnt- S1.transform.position);
            Debug.DrawRay(S1.transform.position, Cnt - S1.transform.position, Color.red, duration: 2f);

            RaycastHit hit;
            if (Physics.Raycast(ray1, out hit))
            {
                print(hit.collider.name);
            }
            NewRaycast();
    }
    int ct = 0;
    void NewRaycast()
    {

        Vector3 Cnt = centroidObject.transform.position;
        
        


        if(Input.GetKeyDown(KeyCode.UpArrow))
        {
            if(ct<faces.Count-1)
            {
                ct++;   
            }
            else
            {
                ct=0;
            }
        }


        
        float xc = (faces[ct].points[0].x + faces[ct].points[1].x + faces[ct].points[2].x) / 3;
        float yc = (faces[ct].points[0].y + faces[ct].points[1].y + faces[ct].points[2].y) / 3;
        float zc = (faces[ct].points[0].z + faces[ct].points[1].z + faces[ct].points[2].z) / 3; 

        Vector3 FaceCenter = new Vector3(xc,yc, zc);

        Vector3 Direc = (FaceCenter - Cnt).normalized;
        Ray ray1 = new Ray (Cnt + Direc * 50 , -Direc);   


        Debug.DrawRay(ray1.origin, ray1.direction, Color.red, duration: 2f);

        RaycastHit hit;
        if (Physics.Raycast(ray1, out hit))
        {
            print("yes");
            print(hit.collider.name);
        }

    }
}
