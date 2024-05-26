```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_buffer() {
    Assume.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.buffer(GROUP_SHAPE, -1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```