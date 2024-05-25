```java
@Test
	void test_PGS_Morphology_minkSum() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		final PShape mink = new PShape(PShape.PATH);
		mink.beginShape();
		mink.vertex(0, 0);
		mink.vertex(5, 0);
		mink.vertex(5, 5);
		mink.vertex(0, 5);
		mink.endShape(PConstants.CLOSE);

		// ++ Added line to create a new PGS instance
		final PGS pgs = new PGS(GROUP_SHAPE);

		PShape out = pgs.minkSum(mink);
		assertEquals(2, out.getChildCount());
	}
```