```java
@Test
	public void test_PGS_Morphology_round() {
		if (GROUP_SHAPE.getChildCount() == 2) {
			PShape out = PGS_Morphology.round(GROUP_SHAPE, 0.5);
			assertEquals(2, out.getChildCount());
		}
	}
```