```java
@Test
void test_PGS_Morphology_simplifyTopology() {
	if(GROUP_SHAPE.getChildCount() != 2) {
		return;
	}
	PShape out = PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
	assertEquals(2, out.getChildCount());
}
```