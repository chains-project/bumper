```java
@Test
	void test_PGS_Morphology_smooth() {
		PShape out = PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
		assertEquals(2, out.getChildCount());
	}
```