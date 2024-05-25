```java
@Test
	void test_PGS_Morphology_buffer() {
		PShape out = PGS_Morphology.buffer(GROUP_SHAPE, -1);
		assertEquals(2, out.getChildCount());
	}
```