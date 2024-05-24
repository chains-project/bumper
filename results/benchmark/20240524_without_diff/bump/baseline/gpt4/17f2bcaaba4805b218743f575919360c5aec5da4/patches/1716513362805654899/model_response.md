```java
  @Test
	void test_PGS_Morphology_smoothGaussian() {
		org.junit.Assume.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
		assertEquals(2, out.getChildCount());
	}
```