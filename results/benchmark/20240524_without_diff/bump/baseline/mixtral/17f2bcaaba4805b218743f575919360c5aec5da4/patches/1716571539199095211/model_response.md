Here's a proposed patch for the failing client code:

```java
@Test
void test_PGS_Morphology_simplifyTopology() {
    // Make sure the child count is 2 before proceeding
    assumeTrue(getChildCount(GROUP_SHAPE) == 2);
    
    // Use the static method to simplify topology
    PShape out = PGS_Morphology.simplifyTopology(GROUP_SHAPE, 1);
    
    // Assert the child count after simplification
    assertEquals(2, getChildCount(out));
}

// Add helper method to get child count
private int getChildCount(PShape shape) {
    return shape.getChildCount();
}
```

This patch introduces a helper method `getChildCount` to avoid the direct usage of the `getChildCount` method from the `PShape` class. This should resolve the "cannot find symbol" error.