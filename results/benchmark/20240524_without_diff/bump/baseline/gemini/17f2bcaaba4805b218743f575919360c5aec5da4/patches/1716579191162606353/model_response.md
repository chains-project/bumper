```java
@Test
	void test_PGS_Morphology_simplifyVW() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.simplifyVW(GROUP_SHAPE, 1);
		assertEquals(2, out.getChildCount());
	}
```