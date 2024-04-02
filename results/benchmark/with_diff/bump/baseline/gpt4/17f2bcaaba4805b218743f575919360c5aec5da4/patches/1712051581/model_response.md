```java
@Test
void test_PGS_Morphology_radialWarp() {
    boolean condition = GROUP_SHAPE.getChildCount() == 2;
    if (!condition) throw new AssumptionViolatedException("Assumption failed", condition);
    PShape out = PGS_Morphology.radialWarp(GROUP_SHAPE, 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```