Here's a fixed version of the method using `assert` instead of `Assume.assumeTrue`:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyTopology() {
    assert GROUP_SHAPE.getChildCount() == 2;
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```
The `Assume` class is not needed in this case, and the test will fail if the assertion is not true. This should fix the "cannot find symbol" error.