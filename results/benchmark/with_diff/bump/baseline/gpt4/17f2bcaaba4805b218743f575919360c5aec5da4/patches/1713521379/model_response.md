```java
@Test
void test_PGS_Morphology_smooth() {
	if (GROUP_SHAPE.getChildCount() != 2) {
		return;
	}
	PShape out = PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
	assertEquals(2, out.getChildCount());
}
```