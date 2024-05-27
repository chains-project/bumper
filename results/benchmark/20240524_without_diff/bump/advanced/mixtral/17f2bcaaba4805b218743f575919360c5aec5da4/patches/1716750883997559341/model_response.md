Here's a fixed version of the code that replaces the failing `Assume.assumeTrue` method with a JUnit 5 `assertAll` method:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_simplifyVW() {
    boolean condition = GROUP_SHAPE.getChildCount() == 2;
    org.junit.jupiter.api.Assertions.assertAll(
        () -> org.junit.jupiter.api.Assertions.assertTrue(condition),
        () -> {
            processing.core.PShape out = micycle.pgs.PGS_Morphology.simplifyVW(GROUP_SHAPE, 1);
            org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
        }
    );
}
```

This code first checks the condition `GROUP_SHAPE.getChildCount() == 2` using an `assertAll` method, which takes a vararg of `Executable` objects. If the condition is false, the test will fail. If the condition is true, the test will continue executing the next `Executable` object, which is the original test code that calls `PGS_Morphology.simplifyVW` method.