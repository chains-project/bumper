```java
@Test
	void test_PGS_Morphology_round() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.round(GROUP_SHAPE, 0.5);
		assertEquals(2, out.getChildCount());
	}
```