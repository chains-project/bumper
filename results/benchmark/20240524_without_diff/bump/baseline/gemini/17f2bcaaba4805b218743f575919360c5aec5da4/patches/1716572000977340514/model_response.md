```java
  @Test
	void test_PGS_Morphology_chaikinCut() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = new PShape();
		out.addChild(PGS_Morphology.chaikinCut(GROUP_SHAPE.getChild(0), 0.5, 2));
		out.addChild(PGS_Morphology.chaikinCut(GROUP_SHAPE.getChild(1), 0.5, 2));
		assertEquals(2, out.getChildCount());
	}
```