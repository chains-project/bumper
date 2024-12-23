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

		// Create a new PShape object to store the result of the minkDifference operation.
		PShape out = new PShape(PShape.GROUP);

		// Iterate over the children of the GROUP_SHAPE and perform the minkDifference operation on each child.
		for (int i = 0; i < GROUP_SHAPE.getChildCount(); i++) {
			PShape child = GROUP_SHAPE.getChild(i);
			PShape childOut = PGS_Morphology.minkDifference(child, mink);
			out.addChild(childOut);
		}

		assertEquals(2, out.getChildCount());
	}
```