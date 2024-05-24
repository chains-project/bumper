```java
@Test
	public void test_PGS_Morphology_simplifyTopology() {
		PShape shape = PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
		assertEquals(2, shape.getChildCount());
	}
```