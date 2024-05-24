```java
@Test
void test_PGS_Morphology_minkDifference() {
	Assumptions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
	final PShape mink = new PShape(PShape.PATH);
	mink.beginShape();
	mink.vertex(0, 0);
	mink.vertex(5, 0);
	mink.vertex(5, 5);
	mink.vertex(0, 5);
	mink.endShape(PConstants.CLOSE);

	PShape out = PGS_Morphology.minkDifference(GROUP_SHAPE, mink);
	assertEquals(2, out.getChildCount());
}
```