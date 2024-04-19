Since the package `develop.p2p.lib` does not exist, you might want to check if the package name has been changed or if the function `sigmoid` has been moved to a different package. If the function `sigmoid` is now in the package `ml.peya.lib`, the import statement would change to:

```java
import static ml.peya.lib.LearnMath.sigmoid;
```