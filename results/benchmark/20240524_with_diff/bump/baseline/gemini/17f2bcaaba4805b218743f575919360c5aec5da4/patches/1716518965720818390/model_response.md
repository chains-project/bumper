```java
@Test
	public void test_PGS_Morphology_smoothGaussian() {
		PShape out = PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
		assertEquals(2, out.getChildCount());
	}
```