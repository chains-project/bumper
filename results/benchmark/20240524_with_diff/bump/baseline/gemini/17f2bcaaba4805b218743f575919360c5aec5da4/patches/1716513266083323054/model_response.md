```java
@Test
	void test_PGS_Morphology_chaikinCut() {
		assumeTrue(true);
		PShape out = PGS_Morphology.chaikinCut(GROUP_SHAPE, 0.5, 2);
		assertEquals(2, out.getChildCount());
	}
```