Here's the fixed method with the necessary import statement added:

```java
import static org.junit.jupiter.api.Assertions.assumeTrue;

@org.junit.jupiter.api.Test
void test_PGS_Morphology_round() {
    assumeTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.round(GROUP_SHAPE, 0.5);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The error was caused because the `assumeTrue` method from JUnit Jupiter was not imported. By adding the import statement, the code should now compile and run successfully.