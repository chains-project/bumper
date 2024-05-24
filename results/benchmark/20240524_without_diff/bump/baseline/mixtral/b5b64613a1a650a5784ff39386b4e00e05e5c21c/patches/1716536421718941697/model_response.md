Here's the proposed patch:

```java
import static org.apache.commons.lang3.StringUtils.isAnyBlank;

// ...

if (isAnyBlank(fieldValue, defaultValue)) {
    // ...
}
```

This patch replaces the usage of the `isAllBlank` method with the `isAnyBlank` method from the same `StringUtils` class. This should resolve the compilation error caused by the upgrade.