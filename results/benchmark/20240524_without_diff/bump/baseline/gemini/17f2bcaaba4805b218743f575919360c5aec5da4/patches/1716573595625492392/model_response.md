```java
@Test
	void test_PGS_Morphology_simplify() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);
		PShape out = PGS_Morphology.simplify(GROUP_SHAPE, 1);
		assertEquals(2, out.getChildCount());
		assertEquals(GROUP_SHAPE.getChild(0).getShapeType(), out.getChild(0).getShapeType());
		assertEquals(GROUP_SHAPE.getChild(1).getShapeType(), out.getChild(1).getShapeType());
	}
```