Here's a possible patch for the failing client code:

```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;
```

This patch replaces the failing import statement with a new one that imports the `isAllBlank` method from the `org.apache.commons.lang3.StringUtils` class. The `org.apache.commons.text` package has been replaced with `org.apache.commons.lang3`, which should be available in the new version.

Note that the `isAllBlank` method has the same functionality in both packages, so the code should work as expected.