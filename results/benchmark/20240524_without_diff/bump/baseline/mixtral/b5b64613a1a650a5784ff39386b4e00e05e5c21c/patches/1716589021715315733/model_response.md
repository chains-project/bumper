Here's the proposed patch for the failing client code:

```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;
```

This patch replaces the failing import statement with a new one that uses the `StringUtils` class from the `org.apache.commons.lang3` package instead of `org.apache.commons.text`. The `isAllBlank` method is available in both packages, so this change should not affect the functionality of the code.