Here is a proposed patch for the failing client code:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_fieldWarp() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.fieldWarp(GROUP_SHAPE, 10, 1, false);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The failure is caused by the use of the `Assume` class from JUnit 4, which is not available in JUnit 5. The `assumeTrue` method should be replaced with the equivalent method from the `Assertions` class in JUnit Jupiter.