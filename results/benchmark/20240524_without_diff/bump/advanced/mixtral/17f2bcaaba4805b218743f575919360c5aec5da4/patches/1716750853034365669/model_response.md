Here's the fixed `test_PGS_Morphology_simplifyVW` method:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyVW() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyVW(GROUP_SHAPE, 1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

In the original code, `Assume.assumeTrue` was used from JUnit 4, but the test framework being used here is JUnit Jupiter (JUnit 5). The method `assumeTrue` should be imported from `org.junit.jupiter.api.Assertions` instead.