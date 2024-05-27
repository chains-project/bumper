Here's the patched version of the code:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smooth() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

In the original code, the method `assumeTrue` is from JUnit 4, but the test is being run with JUnit 5. The `assumeTrue` method in JUnit 5 is part of `Assertions`, not `Assume`. Therefore, I replaced `Assume.assumeTrue` with `Assertions.assumeTrue`.