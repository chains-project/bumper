```java
  @Test
	void test_PGS_Morphology_chaikinCut() {
		PShape shape = GROUP_SHAPE.getChild(0);
		PShape out = PGS_Morphology.chaikinCut(shape, 0.5, 2);
		assertEquals(2, out.getChildCount());
	}
```