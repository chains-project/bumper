```java
@Test
void testAreaMerge() {
    PShape mesh = PGS_Triangulation.delaunayTriangulation(PGS_PointSet.random(0, 0, 1000, 1000, 1111, 0));
    List<PShape> faces = PGS_Conversion.getChildren(mesh);
    faces.sort((a, b) -> Double.compare(PGS_ShapePredicates.area(a), PGS_ShapePredicates.area(b)));
    double areaThreshold = PGS_ShapePredicates.area(faces.get(faces.size() / 2));

    List<PShape> mergedFaces = new ArrayList<>();
    for (PShape face : faces) {
        if (PGS_ShapePredicates.area(face) >= areaThreshold) {
            mergedFaces.add(face);
        }
    }
    PShape mergedMesh = PGS_Conversion.merge(mergedFaces);
    assertTrue(mergedFaces.stream().allMatch(f -> PGS_ShapePredicates.area(f) >= areaThreshold));
    assertTrue(faces.size() >= mergedMesh.getChildCount());
    assertEquals(PGS_ShapePredicates.area(mesh), PGS_ShapePredicates.area(mergedMesh), 1e-6);
}
```