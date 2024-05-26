Here's the updated code that should fix the illegal start of expression error and be compatible with the new library version:

```java
@org.junit.jupiter.api.Test
@org.junit.Ignore
void testRobustnessRandomly() {
    java.util.Random r = new it.unimi.dsi.util.XoRoShiRo128PlusRandom(0);
    int k = nodedEdges = 
```