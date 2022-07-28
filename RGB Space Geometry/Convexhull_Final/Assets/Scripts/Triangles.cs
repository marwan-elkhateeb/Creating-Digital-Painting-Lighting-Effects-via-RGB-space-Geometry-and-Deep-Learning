using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;

public class face
{
    // points of faces (3 points)
    public List<Vector3> points = new List<Vector3>();
}




public class Triangles : MonoBehaviour
{
    public GameObject MeshObject;
    List<GameObject> TRImesh = new List<GameObject>();
    List<Mesh> meshh = new List<Mesh>();
    Vector3[] vertices;
    int[] triangles;
    
    public CentroidColor centroidColorScript;

    // Start is called before the first frame update
    void Start()
    {
        string path = "_Triangles.txt";
        readTextFile(path);
        DrawTri();
        CreateMyMesh();
        
        
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
            string[] arr = inp_ln.Replace("a", "").Replace("b", "").Replace("c", "").Replace(" ", "").Replace("=", "")
                .Replace("]", "").Replace("[", "").Split(',');
            Vector3 pos = new Vector3(float.Parse(arr[0]), float.Parse(arr[1]), float.Parse(arr[2]));
            GameObject sphere = GameObject.CreatePrimitive(PrimitiveType.Sphere);
            sphere.transform.position = pos;
            sphere.GetComponent<Renderer>().material.color = new Color32(byte.Parse(Convert.ToInt32(pos[0]).ToString()),
                byte.Parse(Convert.ToInt32(pos[1]).ToString()), byte.Parse(Convert.ToInt32(pos[2]).ToString()), 255);
            sphere.transform.localScale = new Vector3(2f, 2f, 2f);
            vec.Add(pos);
            pnn.points.Add(pos);
            Count++;
            if (Count == 3)
            {
                faces.Add(pnn);
                pnn = new face();
                Count = 0;
            }
        }





        inp_stm.Close();


    }
    void DrawTri()
    {
        for (int i = 0; i < faces.Count; i++)
        {
            Debug.DrawLine(faces[i].points[0], faces[i].points[1], new Color32(byte.Parse(Convert.ToInt32(faces[i].points[0].x).ToString()),
                byte.Parse(Convert.ToInt32(faces[1].points[0].y).ToString()), byte.Parse(Convert.ToInt32(faces[i].points[0].z).ToString()), 255), 0.04f);
            Debug.DrawLine(faces[i].points[1], faces[i].points[2], new Color32(byte.Parse(Convert.ToInt32(faces[i].points[1].x).ToString()),
                byte.Parse(Convert.ToInt32(faces[1].points[1].y).ToString()), byte.Parse(Convert.ToInt32(faces[i].points[1].z).ToString()), 255), 0.04f);
            Debug.DrawLine(faces[i].points[2], faces[i].points[0], new Color32(byte.Parse(Convert.ToInt32(faces[i].points[2].x).ToString()),
                byte.Parse(Convert.ToInt32(faces[1].points[2].y).ToString()), byte.Parse(Convert.ToInt32(faces[i].points[2].z).ToString()), 255), 0.04f);


        }

    }
    Vector3 centroid = new Vector3((float)82.8456911, (float)128.72690995, (float)150.07576903);
    int isExist(Vector3 v, List<Vector3> tmpVec)
    {
        for (int i = 0; i < tmpVec.Count; i++)
        {
            if (v.x == tmpVec[i].x
                && v.y == tmpVec[i].y
                && v.z == tmpVec[i].z
                )
                return i;
        }
        return -1;
    }
    void CreateMyMesh()
    {

        meshh = new List<Mesh>();
        List<Vector3> tmpVec = new List<Vector3>();
        List<int> tmpTriangles = new List<int>();
        for (int i = 0; i < faces.Count; i++)
        {
            if (faces[i].points.Count == 3)
            {
                Vector3 DirectionnnOFTRI = Vector3.Cross(faces[i].points[1] - faces[i].points[0], faces[i].points[2] - faces[i].points[0]).normalized;

                Vector3 CentroidTRI = new Vector3((faces[i].points[0].x + faces[i].points[1].x + faces[i].points[2].x) / 3
                , (faces[i].points[0].y + faces[i].points[1].y + faces[i].points[2].y) / 3
                , (faces[i].points[0].z + faces[i].points[1].z + faces[i].points[2].z) / 3);
                float Sign = Vector3.Dot(DirectionnnOFTRI, centroid - CentroidTRI);
                if (Sign > 0)
                {
                    for (int j = 2; j >= 0; j--)
                    {
                        Vector3 v = new Vector3(faces[i].points[j].x, faces[i].points[j].y, faces[i].points[j].z);
                        int iWhich = isExist(v, tmpVec);
                        if (iWhich == -1)
                        {
                            tmpVec.Add(v);
                            tmpTriangles.Add(tmpVec.Count - 1);
                        }
                        else
                        {
                            tmpTriangles.Add(iWhich);
                        }
                    }
                }
                else
                {
                    for (int j = 0; j < 3; j++)
                    {
                        Vector3 v = new Vector3(faces[i].points[j].x, faces[i].points[j].y, faces[i].points[j].z);
                        int iWhich = isExist(v, tmpVec);
                        if (iWhich == -1)
                        {
                            tmpVec.Add(v);
                            tmpTriangles.Add(tmpVec.Count - 1);
                        }
                        else
                        {
                            tmpTriangles.Add(iWhich);
                        }
                    }
                }
            }
            else
            {
                print("Error : #of points in Face != 3");
            }
            GameObject newMeshObject = Instantiate(MeshObject, MeshObject.transform.position, Quaternion.identity);
            newMeshObject.name = "triangle number " + i;
            //newMeshObject.GetComponent<MeshCollider>().convex= true;
            Mesh mesh = new Mesh();
            //newMeshObject.GetComponent<MeshRenderer>().material.color = new Color(tmpVec[0].x, tmpVec[0].y, tmpVec[0].z, 1f);
            newMeshObject.GetComponent<MeshFilter>().mesh = mesh;
            newMeshObject.GetComponent<MeshCollider>().sharedMesh = mesh;
            mesh.Clear();
            mesh.vertices = tmpVec.ToArray();
            mesh.triangles = tmpTriangles.ToArray();
            mesh.RecalculateNormals();
            mesh.name = "triangle mesh number " + i;


            TRImesh.Add(newMeshObject);
            tmpVec.Clear();
            tmpTriangles.Clear();
            MeshColor(mesh);

        }

    }



    void Checkk()
    {
        print(" Mesh count =  " + meshh.Count);
        if (Input.GetKeyDown(KeyCode.DownArrow))
        {
            CreateMyMesh();
        }
    }
    // Update is called once per frame
    void FixedUpdate()
    {
        //Checkk();
        DrawTri();

        
        
       // centroidColorScript.Raycasttt();
    }
    void MeshColor(Mesh mesh)
    {

        Vector3[] vertices = mesh.vertices;

        // create new colors array where the colors will be created.
        Color[] colors = new Color[vertices.Length];

        for (int i = 0; i < vertices.Length; i++)
        {
            
             colors[i] = new Color32(byte.Parse(Convert.ToInt32(vertices[i].x).ToString()), byte.Parse(Convert.ToInt32(vertices[i].y).ToString()),
                 byte.Parse(Convert.ToInt32(vertices[i].z).ToString()), 255);

        }
        
        // assign the array of colors to the Mesh.
        mesh.colors = colors;
    }
}
