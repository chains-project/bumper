Here's a patch that you can apply to fix the error:

```java
import static org.apache.commons.lang3.StringUtils.isAnyBlank;

// replace all occurrences of 'isAllBlank' with 'isAnyBlank'
```

This patch replaces the failing method `isAllBlank` with a new method `isAnyBlank` from the same library. You can replace all occurrences of `isAllBlank` with `isAnyBlank` to fix the error.