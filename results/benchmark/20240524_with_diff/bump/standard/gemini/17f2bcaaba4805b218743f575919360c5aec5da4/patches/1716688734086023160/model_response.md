```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_buffer() {
    processing.core.PShape out = micycle.pgs.PGS_Morphology.buffer(GROUP_SHAPE, -1);
    assertEquals(2, out.getChildCount());
}
```