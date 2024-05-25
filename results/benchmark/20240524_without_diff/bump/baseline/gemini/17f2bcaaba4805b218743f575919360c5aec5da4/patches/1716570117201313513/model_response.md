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

		PShape out = new PShape(PShape.PATH);
		out.beginShape();
		out.vertex(0, 0);
		out.vertex(5, 0);
		out.vertex(5, 5);
		out.vertex(0, 5);
		out.endShape(PConstants.CLOSE);

		PShape out2 = new PShape(PShape.PATH);
		out2.beginShape();
		out2.vertex(0, 0);
		out2.vertex(5, 0);
		out2.vertex(5, 5);
		out2.vertex(0, 5);
		out2.endShape(PConstants.CLOSE);

		assertEquals(2, out.getChildCount());
		assertEquals(2, out2.getChildCount());
	}
```