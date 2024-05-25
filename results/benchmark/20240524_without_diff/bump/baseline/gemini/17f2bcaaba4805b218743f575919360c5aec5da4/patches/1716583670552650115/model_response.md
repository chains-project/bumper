```java
@Test
	void test_PGS_Processing_removeSmallHoles() {
		PShape groupShape = GROUP_SHAPE;
		assumeTrue(groupShape.getChildCount() == 2);
		PShape out = PGS_Processing.removeSmallHoles(groupShape, 10);
		assertEquals(2, out.getChildCount());
	}
```