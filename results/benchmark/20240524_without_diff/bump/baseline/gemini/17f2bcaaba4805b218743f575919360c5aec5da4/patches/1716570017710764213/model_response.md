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

		// Add a child to the mink shape
		final PShape child = new PShape(PShape.GROUP);
		child.addChild(mink);
		mink.addChild(child);

		PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);
		assertEquals(2, out.getChildCount());
	}
```