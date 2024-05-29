Here's a fixed version of the `test_PGS_Morphology_buffer` method using `import static` for the `assumeTrue` method:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_buffer() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.buffer(GROUP_SHAPE, -1);
    assertEquals(2, out.getChildCount());
}
```

This code imports the `assumeTrue` method from `org.junit.jupiter.api.Assumptions` and uses it in the test method. This should fix the "cannot find symbol" error.