```java
@org.junit.jupiter.api.Test
void test_PGS_Processing_densify() {
    if (GROUP_SHAPE.getChildCount() != 2) {
        throw new RuntimeException("GROUP_SHAPE.getChildCount() != 2");
    }
    processing.core.PShape out = micycle.pgs.PGS_Processing.densify(GROUP_SHAPE, 1);
    assertEquals(2, out.getChildCount());
}
```