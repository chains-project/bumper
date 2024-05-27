Here's the fixed version of the code, using `org.junit.jupiter.api.Assertions.assertTrue` instead of `org.junit.Assume.assumeTrue`:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    boolean condition = GROUP_SHAPE.getChildCount() == 2;
    org.junit.jupiter.api.Assertions.assertTrue(condition);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

This code change makes sure that the test fails gracefully if the condition is not met, instead of throwing an error.