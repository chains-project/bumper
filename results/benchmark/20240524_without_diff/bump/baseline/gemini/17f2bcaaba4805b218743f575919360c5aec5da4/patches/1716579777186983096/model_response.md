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

		// Create a new PShape object to hold the result of the minkDifference operation.
		PShape out = new PShape();

		// Call the minkDifference method on the PGS_Morphology class, passing in the GROUP_SHAPE and mink objects.
		// The result is stored in the out object.
		PGS_Morphology.minkDifference(GROUP_SHAPE, mink, out);

		// Assert that the out object has two child shapes.
		assertEquals(2, out.getChildCount());
	}
```