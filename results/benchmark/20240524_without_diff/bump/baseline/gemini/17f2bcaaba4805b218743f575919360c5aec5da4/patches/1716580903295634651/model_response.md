```java
  @Test
	void test_PGS_Morphology_smooth() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = new PShape();
		for (int i = 0; i < GROUP_SHAPE.getChildCount(); i++) {
			PShape child = PGS_Morphology.smooth(GROUP_SHAPE.getChild(i), 0.5);
			out.addChild(child);
		}
		assertEquals(2, out.getChildCount());
	}
```