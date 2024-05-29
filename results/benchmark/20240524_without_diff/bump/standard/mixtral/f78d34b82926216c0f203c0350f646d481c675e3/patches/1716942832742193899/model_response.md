Here's the proposed patch for the failing client code:

```java
import static org.apache.commons.math3.ml.stat.DescriptiveStatistics.sigmoid;
```

Note: I replaced the non-existent package `develop.p2p.lib` with `org.apache.commons.math3.ml.stat`, which contains the `sigmoid` method. You may need to add the corresponding dependency to your project to use this package.