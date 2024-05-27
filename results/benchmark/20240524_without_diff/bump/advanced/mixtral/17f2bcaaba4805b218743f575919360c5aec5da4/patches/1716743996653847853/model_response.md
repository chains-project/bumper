Here's the fixed version of the `test_PGS_Morphology_buffer` method:

```java
@org.junit.jupiter.api.Test
void test_PGS_Morphology_buffer() {
    org.junit.jupiter.api.Assertions.assertTrue(GROUP_SHAPE.getChildCount() == 2);
    processing.core.PShape out = micycle.pgs.PGS_Morphology.buffer(GROUP_SHAPE, -1);
    org.junit.jupiter.api.Assertions.assertEquals(2, out.getChildCount());
}
```

The error message suggests that the `assumeTrue` method is not found, which is part of JUnit 4. In this case, we can replace it with the `assertTrue` method from JUnit Jupiter (JUnit 5).