```java
@Test
	void test_PGS_Processing_removeSmallHoles() {
		assumeTrue(GROUP_SHAPE.getChildCount() == 2);

		// Create a copy of the GROUP_SHAPE
		PShape copy = new PShape();
		for (PShape child : GROUP_SHAPE.getChildren()) {
			copy.addChild(child.copy());
		}

		PShape out = PGS_Processing.removeSmallHoles(copy, 10);
		assertEquals(2, out.getChildCount());
	}
```