```java
@Test
	void test_PGS_Processing_convexPartition() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape[] shapes = new PShape[2];
		GROUP_SHAPE.getChildren(shapes);
		PShape out = PGS_Processing.convexPartition(shapes[0], shapes[1]);
		assertEquals(2, out.getChildCount());
	}
```