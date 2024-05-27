Here is the proposed patch for the failing client code:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assumptions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_smoothGaussian() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    assertEquals(2, out.getChildCount());
}
```

The issue with the original code is that it is using the `Assume` class from JUnit 4, while the test is being executed with JUnit 5. To fix this, I have imported the `assumeTrue` method from JUnit 5's `Assumptions` class and replaced the `Assume.assumeTrue` call with `assumeTrue`.

Note that I have also imported the `assertEquals` method from JUnit 5's `Assertions` class to ensure that the correct version of this method is being used.