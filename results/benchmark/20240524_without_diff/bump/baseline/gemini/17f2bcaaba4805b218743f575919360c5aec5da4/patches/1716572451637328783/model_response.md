```java
@Test
	void test_PGS_Morphology_fieldWarp() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.fieldWarp(GROUP_SHAPE.getChild(0), 10, 1, false);
		assertEquals(1, out.getChildCount());
	}
```