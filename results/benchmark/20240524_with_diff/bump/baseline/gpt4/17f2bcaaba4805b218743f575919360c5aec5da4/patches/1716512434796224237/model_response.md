```java
@Test
void test_PGS_Morphology_erosionDilation() {
    boolean assumption = GROUP_SHAPE.getChildCount() == 2;
    if (!assumption) {
        throw new AssumptionViolatedException("Assumption failed");
    }
    PShape out = PGS_Morphology.erosionDilation(GROUP_SHAPE, 0);
    assertEquals(2, out.getChildCount());
}
```