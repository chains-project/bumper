```java
@Test
void test_PGS_Morphology_erosionDilation() {
	if (GROUP_SHAPE.getChildCount() != 2) {
		return;
	}
	PShape out = PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
	assertEquals(2, out.getChildCount());
}
```