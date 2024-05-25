Here's a patch that you can apply to fix the error:

```java
import new.develop.p2p.lib.WaveCreator;
```

This patch imports the `WaveCreator` class from the new location `new.develop.p2p.lib` instead of `develop.p2p.lib`. The failure is likely caused by a change in the external dependency's package structure. This patch should fix the issue by updating the import statement accordingly.