```java
	@Test
	void test_PGS_Morphology_smooth() {
		PShape shape = GROUP_SHAPE.getChild(0);
		PShape out = PGS_Morphology.smooth(shape, 0.5);
		assertEquals(1, out.getChildCount());
	}
```