```java
@Test
	void testAreaMerge() {
		PShape mesh = PGS_Triangulation.delaunayTriangulation(PGS_PointSet.random(0, 0, 1000, 1000, 1111, 0));
		List<PShape> faces = PGS_Conversion.getChildren(mesh);
		faces.sort((a, b) -> Double.compare(PGS_ShapePredicates.area(a), PGS_ShapePredicates.area(b)));
		double areaThreshold = PGS_ShapePredicates.area(faces.get(faces.size() / 2));

		PShape mergedMesh = PGS_Meshing.areaMerge(mesh, areaThreshold);

		// Check that all faces in the merged mesh have an area greater than or equal to the threshold
		assertTrue(PGS_Conversion.getChildren(mergedMesh).stream().allMatch(f -> PGS_ShapePredicates.area(f) >= areaThreshold));

		// Check that the number of faces in the merged mesh is less than or equal to the number of faces in the original mesh
		assertTrue(faces.size() >= mergedMesh.getChildCount());

		// Check that the area of the merged mesh is equal to the area of the original mesh
		assertEquals(PGS_ShapePredicates.area(mesh), PGS_ShapePredicates.area(mergedMesh), 1e-6);
	}
```