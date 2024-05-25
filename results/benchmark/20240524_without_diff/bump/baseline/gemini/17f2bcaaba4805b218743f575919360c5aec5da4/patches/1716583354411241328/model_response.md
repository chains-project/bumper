```java
@Test
	void test_PGS_Processing_densify() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Processing.densify(GROUP_SHAPE, 1);
		assertEquals(2, out.getChildCount());
	}
```