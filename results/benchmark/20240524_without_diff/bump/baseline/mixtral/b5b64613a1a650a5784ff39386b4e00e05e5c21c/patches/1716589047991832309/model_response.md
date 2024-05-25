Here's a patch that you can apply to the code in order to fix the error:

```java
import static org.apache.commons.lang3.StringUtils.isAllBlank;
```

In this patch, we replace the `org.apache.commons.text.StringUtils` class with the `org.apache.commons.lang3.StringUtils` class, which provides the same `isAllBlank` method. This should resolve the error message you encountered, as the `org.apache.commons.lang3` package is a different package than `org.apache.commons.text`, but it provides similar functionality.