Here's the proposed patch to fix the error:

```java
import new.dependency.WaveCreator;
```

Please replace the original import statement with the above line. The `develop.p2p.lib` dependency seems to be broken, so I replaced it with `new.dependency` which should be the new package where `WaveCreator` is located.