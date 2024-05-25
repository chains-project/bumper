```java
  @Test
  void test_PGS_Morphology_smoothGaussian() {
    PShape shape = PGS_Morphology.smoothGaussian(GROUP_SHAPE, 10);
    assertEquals(2, shape.getChildCount());
  }
```