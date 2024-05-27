Here's a fixed version of the code that uses `org.junit.jupiter.api.Assertions.assertTrue` instead of `org.junit.Assume.assumeTrue`:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smooth() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The reason for the error is that `org.junit.Assume.assumeTrue` is not part of JUnit 5, which is what the `@org.junit.jupiter.api.Test` annotation indicates. Instead, you can use `org.junit.jupiter.api.Assertions.assertTrue` to assert that a condition is true.