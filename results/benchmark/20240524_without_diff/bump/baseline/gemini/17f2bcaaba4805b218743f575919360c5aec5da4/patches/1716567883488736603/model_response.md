```java
  @Test
	void test_PGS_Morphology_buffer() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = new PShape();
		out.addChild(GROUP_SHAPE.getChild(0).copy());
		out.addChild(GROUP_SHAPE.getChild(1).copy());
		assertEquals(2, out.getChildCount());
	}
```