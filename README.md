# Creating-Digital-Painting-Lighting-Effects-via-RGB-space-Geometry-and-Deep-Learning
This project presents a solution to relighting drawings, comparing deep learning with traditional methods (Mathematical). Where the traditional plots image pixels in 3D space, generates a convex hull using the pixels as vertices, calculates convex centroid and casts a ray towards calculated directions and generate intersections, produces stroke density map, normalizes original image to reduce noise and generate coarse-lighting effects, refines the last output to ensure shading matches intensities, and lastly multiplies refinements for the result. Whereas Deep learning model generates four images with different lighting effects.

## System Overview
![System Overview](https://user-images.githubusercontent.com/60660907/181640993-06b97ac0-d91e-44b0-aabf-b0b63266924e.JPG)

## Class Digaram for RGB Space Geometry 
![ClassDiagram1](https://user-images.githubusercontent.com/60660907/181636444-3ce4a8c7-4953-4b53-ac36-7ebef76088f6.png)

## Extracting Palette 
![Extract palette](https://user-images.githubusercontent.com/60660907/181640414-94be06d6-7619-414e-82e9-c12d05d97dbd.JPG)

## Convex-Hull for palette
![Centroid](https://user-images.githubusercontent.com/60660907/181640491-eb3a966d-c86c-493e-9552-cda854c0e436.JPG)

## Example 1 for a gradint mesh
![Example for mesh](https://user-images.githubusercontent.com/60660907/181640574-c28dfe1c-789b-48a5-8749-70aadd80a3ec.JPG)

## Example 2 for a gradint mesh 
![Example for mesh 2](https://user-images.githubusercontent.com/60660907/181640604-4f011bd3-77a0-413c-a8e9-33a20f29b13e.JPG)

## Example 1 for UI 
![Testing image 1 with UI](https://user-images.githubusercontent.com/60660907/181641089-c2f547a7-c379-46d3-9256-48164618b36e.JPG)

## Example 2 for UI
### Showning Stroke Density map of the input image
![Testing image 2 with UI](https://user-images.githubusercontent.com/60660907/181641125-7d954f19-1d59-472c-a514-617d460f6cc9.JPG)

## Deep Learning Results
![Deep learning resuts](https://user-images.githubusercontent.com/60660907/181641176-61db88e6-8a75-4be4-9169-027792e4a9d1.JPG)
