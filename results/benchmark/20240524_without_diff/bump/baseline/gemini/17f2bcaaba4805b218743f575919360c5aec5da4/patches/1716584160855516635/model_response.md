```java
@Test
	void test_PGS_Processing_convexPartition() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Processing.convexPartition(GROUP_SHAPE.getChild(0), GROUP_SHAPE.getChild(1));
		assertEquals(2, out.getChildCount());
	}
```