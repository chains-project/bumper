```java
@Test
void test_PGS_Morphology_simplify() {
	assumeThat(GROUP_SHAPE.getChildCount(), is(2));
	PShape out = PGS_Morphology.simplify(GROUP_SHAPE, 1);
	assertEquals(2, out.getChildCount());
}
```