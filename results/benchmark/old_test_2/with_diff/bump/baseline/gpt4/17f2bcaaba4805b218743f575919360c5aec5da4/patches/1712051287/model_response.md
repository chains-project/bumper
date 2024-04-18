```java
@Test
void test_PGS_Morphology_erosionDilation() {
    org.junit.Assume.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    PShape out = PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    assertEquals(2, out.getChildCount());
}
```