```java
  @Test
  public void test_PGS_Morphology_fieldWarp() {
    // Create a new PShape object with two children.
    PShape groupShape = createGroupShapeWithTwoChildren();

    // Perform the fieldWarp operation on the group shape.
    PShape out = PGS_Morphology.fieldWarp(groupShape, 10, 1, false);

    // Assert that the output shape has two children.
    assertEquals(2, out.getChildCount());
  }

  // Helper method to create a PShape object with two children.
  private PShape createGroupShapeWithTwoChildren() {
    PShape groupShape = new PShape();
    groupShape.addChild(new PShape());
    groupShape.addChild(new PShape());
    return groupShape;
  }
```