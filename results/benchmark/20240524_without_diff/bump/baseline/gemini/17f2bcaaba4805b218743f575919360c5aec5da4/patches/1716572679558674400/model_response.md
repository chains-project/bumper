```java
@Test
	void test_PGS_Morphology_minkDifference() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		final PShape mink = new PShape(PShape.PATH);
		mink.beginShape();
		mink.vertex(0, 0);
		mink.vertex(5, 0);
		mink.vertex(5, 5);
		mink.vertex(0, 5);
		mink.endShape(PConstants.CLOSE);

		PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);

		// Check if the output shape has the expected number of children.
		assertEquals(2, out.getChildCount());

		// Check if the output shape has the expected vertices.
		List<PVector> expectedVertices = Arrays.asList(
				new PVector(0, 0),
				new PVector(5, 0),
				new PVector(5, 5),
				new PVector(0, 5)
		);
		List<PVector> actualVertices = new ArrayList<>();
		for (int i = 0; i < out.getChildCount(); i++) {
			PShape child = (PShape) out.getChild(i);
			if (child.getShapeType() == PShape.PATH) {
				for (int j = 0; j < child.getVertexCount(); j++) {
					actualVertices.add(child.getVertex(j));
				}
			}
		}
		assertEquals(expectedVertices, actualVertices);
	}
```