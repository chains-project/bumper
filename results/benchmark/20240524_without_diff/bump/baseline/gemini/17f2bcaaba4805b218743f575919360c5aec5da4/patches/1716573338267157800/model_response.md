```java
@Test
	void test_PGS_Morphology_radialWarp() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = new PShape();
		out.addChild(PGS_Morphology.radialWarp(GROUP_SHAPE.getChild(0), 10, 1, false));
		out.addChild(PGS_Morphology.radialWarp(GROUP_SHAPE.getChild(1), 10, 1, false));
		assertEquals(2, out.getChildCount());
	}
```