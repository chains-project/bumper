```java
  @Test
	void test_PGS_Morphology_simplify() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.simplify(GROUP_SHAPE, 1);
		assertEquals(1, out.getChildCount());
	}
```