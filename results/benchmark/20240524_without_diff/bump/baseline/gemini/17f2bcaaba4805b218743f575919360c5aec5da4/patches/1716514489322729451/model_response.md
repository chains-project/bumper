```java
@Test
	void test_PGS_Morphology_fieldWarp() {
		// assumeTrue(GROUP_SHAPE.getChildCount() == 2); // Removed method
		int childCount = GROUP_SHAPE.getChildCount();
		assertEquals(2, childCount);
		PShape out = PGS_Morphology.fieldWarp(GROUP_SHAPE, 10, 1, false);
		assertEquals(2, out.getChildCount());
	}
```