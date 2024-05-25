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

		// ++ Add a new PShape variable to hold the result of the minkDifference operation
		PShape out = new PShape();

		// ++ Call the minkDifference method with the new PShape variable as the output parameter
		PGS_Morphology.minkDifference(GROUP_SHAPE, mink, out);

		assertEquals(2, out.getChildCount());
	}
```