```java
@Test
void test_PGS_Morphology_fieldWarp() {
    boolean condition = GROUP_SHAPE.getChildCount() == 2;
    if (!condition) {
        throw new AssumptionViolatedException("Assumption failed");
    }
    PShape out = PGS_Morphology.fieldWarp(GROUP_SHAPE, 10, 1, false);
    assertEquals(2, out.getChildCount());
}
```