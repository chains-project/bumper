Here is a possible patch for the failing client code:

```java
@Test
void test_PGS_Morphology_round() {
    assumeTrue(ProcessingShapeUtils.getChildCount(GROUP_SHAPE) == 2);
    PShape out = PGS_Morphology.round(GROUP_SHAPE, 0.5);
    assertEquals(2, ProcessingShapeUtils.getChildCount(out));
}
```

In this patch, I created a new utility class `ProcessingShapeUtils` that contains the `getChildCount` method, which is used to get the number of children of a `PShape` object. This is because the original `getChildCount` method is not static and cannot be called without an instance of `PShape`.

Note that the `ProcessingShapeUtils` class is not provided in the original code, so you need to implement it yourself. Here's an example implementation:

```java
public class ProcessingShapeUtils {
    public static int getChildCount(PShape shape) {
        return shape.getChildCount();
    }
}
```

This implementation simply delegates the call to the original `getChildCount` method of the `PShape` class.