Here's a possible patch for the given error. I am assuming that the required `StringUtils` class is moved to a different package in the newer version of the library.

```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;
```

This patch replaces the `org.apache.commons.text.StringUtils` import with `org.apache.commons.lang3.StringUtils`. This change should fix the error as long as the required `isAllBlank` method is available in the new package.

If the method is not available in the new package, you may need to find an alternative solution, such as implementing the method yourself or finding a different library that provides the required functionality.