```java
  @Test
	void test_PGS_Morphology_smoothGaussian() {
		if (GROUP_SHAPE.getChildCount() != 2) {
			return;
		}
		PShape out = PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
		assertEquals(2, out.getChildCount());
	}
```