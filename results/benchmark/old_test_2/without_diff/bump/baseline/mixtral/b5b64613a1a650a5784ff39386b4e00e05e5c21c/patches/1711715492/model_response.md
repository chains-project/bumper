Here is a fixed version of the method that should resolve the error:
```java
import static org.apache.commons.lang3.StringUtils.isBlank;

@Override
public CreateJFrogInstanceStepExecution start(StepContext context) throws Exception {
    // Remove the usage of isAllBlank and use isBlank instead
    if (isBlank(serverId) || isBlank(url) || isBlank(apiKey)) {
        throw new InvalidRequestException("Missing parameters to create JFrog instance.");
    }
    // Rest of the method implementation remains unchanged
    ...
}
```
In this fixed version, I replaced the usage of `isAllBlank` with `isBlank` since the former is not present in the newer version of the library. This should resolve the error and make the code compile successfully.