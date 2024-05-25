Here's a patch that you can apply to the code to fix the error:

```java
import org.apache.commons.lang3.StringUtils;

// ...

@Override
public CreateJFrogInstanceStep execute(StepContext context) throws IOException, InterruptedException {
    // ...
    if (isAllBlank(instanceId, url, apiKey)) {
        // ...
    }
    // ...
}

// Remove the static import statement
// static import org.apache.commons.lang3.StringUtils.isAllBlank;
```

This patch imports the `StringUtils` class directly and removes the static import statement for `isAllBlank`. Instead, it uses the fully qualified name of the method `StringUtils.isAllBlank`. This should resolve the "cannot find symbol" error.