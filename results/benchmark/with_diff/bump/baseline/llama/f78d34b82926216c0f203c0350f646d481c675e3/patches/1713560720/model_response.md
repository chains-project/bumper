Here's a proposed patch to fix the error:
```java
import static tokyo.peya.lib.LearnMath.sigmoid;
```
Replace the line:
```java
import static develop.p2p.lib.LearnMath.sigmoid;
```
with the proposed patch. This patch updates the import statement to refer to the new library version's namespace, `tokyo.peya.lib`, instead of the old `develop.p2p.lib`.

The rest of the code remains unchanged.