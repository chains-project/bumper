Here's a patch that you can apply to fix the error:

```java
import org.apache.commons.lang3.StringUtils;

// ...

if (StringUtils.isAllBlank(str1, str2, str3)) {
  // ...
}
```

The change here is to import the `StringUtils` class directly instead of using a static import. This way, the code will still work even if the static import is not available in the new version of the library.