```java
@Test
void test_PGS_Morphology_simplifyVW() {
    PShape shape = new PShape();
    shape.addChild(new PShape());
    shape.addChild(new PShape());
    PShape out = PGS_Morphology.simplifyVW(shape, 1);
    assertEquals(2, out.getChildCount());
}
```