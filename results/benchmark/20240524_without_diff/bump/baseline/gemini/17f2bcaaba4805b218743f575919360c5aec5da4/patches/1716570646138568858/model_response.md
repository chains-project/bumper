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

		final PShape[] children = GROUP_SHAPE.getChildren();
		final PShape firstChild = children[0];
		final PShape secondChild = children[1];

		final PShape out = PGS_Morphology.minkSum(firstChild, mink);
		final PShape out2 = PGS_Morphology.minkSum(secondChild, mink);

		final PShapeGroup outGroup = new PShapeGroup(out);
		outGroup.addChild(out2);

		assertEquals(2, outGroup.getChildCount());
	}
```