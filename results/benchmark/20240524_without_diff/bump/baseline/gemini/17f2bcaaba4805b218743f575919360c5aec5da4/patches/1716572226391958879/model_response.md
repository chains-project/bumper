```java
@Test
	void test_PGS_Morphology_chaikinCut() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		// The following line was modified to fix the error.
		PShape out = PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
		assertEquals(2, out.getChildCount());
	}
```