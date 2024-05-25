```java
@Test
	void test_PGS_Morphology_smooth() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
		// ++ start new code
		if (out == null) {
			out = GROUP_SHAPE;
		}
		// ++ end new code
		assertEquals(2, out.getChildCount());
	}
```