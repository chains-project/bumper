```java
@Test
	void test_PGS_Morphology_radialWarp() {
		if (GROUP_SHAPE.getChildCount() != 2) {
			return;
		}
		PShape out = PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
		assertEquals(2, out.getChildCount());
	}
```