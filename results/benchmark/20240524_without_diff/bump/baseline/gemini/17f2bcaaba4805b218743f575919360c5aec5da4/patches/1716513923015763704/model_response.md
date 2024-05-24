```java
	@Test
	void test_PGS_Morphology_erosionDilation() {
		PShape out = PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
		assertEquals(2, out.getChildCount());
	}
```