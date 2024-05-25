```java
@Test
	void test_PGS_Morphology_round() {
		PShape out = PGS_Morphology.round(GROUP_SHAPE, 0.5);
		assertEquals(2, out.getChildCount());
	}
```