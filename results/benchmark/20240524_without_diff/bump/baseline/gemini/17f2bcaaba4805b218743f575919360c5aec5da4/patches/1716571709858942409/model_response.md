```java
  @Test
	void test_PGS_Morphology_buffer() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = new PShape();
		out.addChild(PGS_Morphology.buffer(GROUP_SHAPE.getChild(0), -1));
		out.addChild(PGS_Morphology.buffer(GROUP_SHAPE.getChild(1), -1));
		assertEquals(2, out.getChildCount());
	}
```