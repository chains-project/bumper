Here's a fixed version of the code that uses the appropriate JUnit 5 assertion:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_buffer() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.buffer(GROUP_SHAPE, -1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

In this updated code, we replaced `org.junit.Assume.assumeTrue` with `org.junit.jupiter.api.Assertions.assertTrue` to perform the assertion.