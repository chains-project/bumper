```java
@org.junit.jupiter.api.Test
void testAreaMerge() {
    processing.core.PShape mesh = micycle.pgs.PGS_Triangulation.delaunayTriangulation(micycle.pgs.PGS_PointSet.random(0, 0, 1000, 1000, 1111, 0));
    java.util.List<processing.core.PShape> faces = micycle.pgs.PGS_Conversion.getChildren(mesh);
    faces.sort(( a, b) -> java.lang.Double.compare(micycle.pgs.PGS_ShapePredicates.area(a), micycle.pgs.PGS_ShapePredicates.area(b)));
    double areaThreshold = micycle.pgs.PGS_ShapePredicates.area(faces.get(faces.size() / 2));
    processing.core.PShape mergedMesh = micycle.pgs.PGS_Meshing.areaMerge(mesh, areaThreshold);
    assertTrue(micycle.pgs.PGS_Conversion.getChildren(mergedMesh).stream().allMatch(( f) -> micycle.pgs.PGS_ShapePredicates.area(f) >= areaThreshold));
    assertTrue(faces.size() >= mergedMesh.getChildCount());
    Assert.assertEquals(micycle.pgs.PGS_ShapePredicates.area(mesh), micycle.pgs.PGS_ShapePredicates.area(mergedMesh), 1.0E-6);
}
```