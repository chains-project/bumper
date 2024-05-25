Here's the proposed patch for the failing client code:

```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;
```

This patch replaces the failed import statement with a new one that imports the `isAllBlank` method from `org.apache.commons.lang3.StringUtils` instead of `org.apache.commons.text.StringUtils`. This should fix the error since the `org.apache.commons.text` package is not found.