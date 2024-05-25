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

		// Create a new PShape object to store the result of the minkDifference operation
		PShape out = new PShape(PShape.PATH);

		// Perform the minkDifference operation on the two PShape objects
		out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);

		// Assert that the resulting PShape object has two children
		assertEquals(2, out.getChildCount());
	}
```