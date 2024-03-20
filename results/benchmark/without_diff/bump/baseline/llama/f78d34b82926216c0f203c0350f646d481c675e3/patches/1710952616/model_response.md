Here's a proposed patch to fix the error:
```java
import static ml.peya.plugins.LearnMath.sigmoid;
```
Explanation:

The error message indicates that the package `develop.p2p.lib` does not exist. After investigating, I found that the `LearnMath` class is part of the `ml.peya.plugins` package. Therefore, I replaced `develop.p2p.lib.LearnMath` with `ml.peya.plugins.LearnMath` in the import statement.

This patch fixes the error by using the correct package name for the `LearnMath` class.