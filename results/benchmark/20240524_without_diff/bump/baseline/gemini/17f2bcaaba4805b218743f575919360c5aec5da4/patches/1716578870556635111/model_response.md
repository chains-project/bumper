```java
@Test
	public void test_PGS_Morphology_simplifyTopology() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
		assertEquals(2, out.getChildCount());
	}
```