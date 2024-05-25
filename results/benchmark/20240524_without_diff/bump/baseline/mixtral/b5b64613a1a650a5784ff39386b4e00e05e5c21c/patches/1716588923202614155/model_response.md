Here's a possible patch for the given failing client code:

```java
import static org.apache.commons.text.StringUtils.isAllBlank;
```

This patch replaces the usage of `org.apache.commons.lang3.StringUtils` with `org.apache.commons.text.StringUtils`, as the `isAllBlank` method has been moved to the latter package in newer versions of Apache Commons Lang.