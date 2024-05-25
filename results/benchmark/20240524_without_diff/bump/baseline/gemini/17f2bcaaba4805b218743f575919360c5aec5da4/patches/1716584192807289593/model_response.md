```java
  @Test
	void test_PGS_Processing_convexPartition() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Processing.convexPartition(GROUP_SHAPE);
		assertEquals(2, out.getChildCount());
		// check if the shapes are convex
		for (int i = 0; i < out.getChildCount(); i++) {
			PShape child = out.getChild(i);
			assertTrue(child.isConvex());
		}
	}
```