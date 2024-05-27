Here is a fixed version of the `test_PGS_Morphology_smooth` method:
```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_smooth() {
    org.junit.jupiter.api.Assertions.assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.smooth(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```
In the original code, the method `assumeTrue` is from JUnit 4's `org.junit.Assume` class, while the test is using JUnit Jupiter (JUnit 5)'s `org.junit.jupiter.api.Test` annotation. In JUnit Jupiter, the equivalent method to `assumeTrue` is also in the `org.junit.jupiter.api.Assertions` class, so the method call should be changed to `Assertions.assumeTrue`.