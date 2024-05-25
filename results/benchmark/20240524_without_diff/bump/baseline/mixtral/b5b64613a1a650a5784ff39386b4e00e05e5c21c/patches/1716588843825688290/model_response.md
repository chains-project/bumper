Here's a possible patch for the given error:

```java
import static org.apache.commons.lang3.StringUtils.isAnyBlank;

//...

@Override
public CreateJFrogInstanceStep executeStep(StepContext context) throws IOException, InterruptedException {
    // Check if 'jfrogInstanceId' and 'url' are not blank
    if (isAnyBlank(jfrogInstanceId, url)) {
        log.error("Missing required parameters: jfrogInstanceId and url.");
        throw new AbortException("Missing required parameters: jfrogInstanceId and url.");
    }

    //...
}
```

In this patch, I replaced the `isAllBlank` method with `isAnyBlank`, which is an added method in the same library version. This should resolve the "cannot find symbol" error.

Note: It is assumed that the missing 'log' variable is defined in the class. If not, you should define it as a `Logger` instance.