```java
@Test
void testAreaMerge() {
    PShape mesh = PGS_Triangulation.delaunayTriangulation(PGS_PointSet.random(0, 0, 1000, 1000, 1111, 0));
    List<PShape> faces = PGS_Conversion.getChildren(mesh);
    faces.sort((a, b) -> Double.compare(PGS_ShapePredicates.area(a), PGS_ShapePredicates.area(b)));
    double areaThreshold = PGS_ShapePredicates.area(faces.get(faces.size() / 2));

    List<PShape> children = PGS_Conversion.getChildren(mesh);
    for (int i = 0; i < children.size(); i++) {
        for (int j = i + 1; j < children.size(); j++) {
            if (PGS_ShapePredicates.area(children.get(i)) + PGS_ShapePredicates.area(children.get(j)) > areaThreshold) {
                children.set(i, PGS_Meshing.union(children.get(i), children.get(j)));
                children.remove(j);
                j--;
            }
        }
    }

    PShape mergedMesh = children.get(0);
    for (int i = 1; i < children.size(); i++) {
        mergedMesh = PGS_Meshing.union(mergedMesh, children.get(i));
    }

    assertTrue(children.stream().allMatch(f -> PGS_ShapePredicates.area(f) >= areaThreshold));
    assertTrue(faces.size() >= children.size());
    assertEquals(PGS_ShapePredicates.area(mesh), PGS_ShapePredicates.area(mergedMesh), 1e-6);
}
```