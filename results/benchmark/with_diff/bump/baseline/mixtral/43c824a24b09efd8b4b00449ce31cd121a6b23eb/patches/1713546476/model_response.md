Here's a proposed patch for the client code:

```java
import de.gwdg.metadataqa.api.json.JsonPath;

// ...

@Override
public JsonBranch getBranch(String path) {
    return JsonPath.compile(path).read(jsonNode);
}
```

In this patch, we import `JsonPath` instead of `JsonBranch` and modify the `getBranch` method to use `JsonPath.compile(path).read(jsonNode)` to achieve the same functionality. This approach avoids using the removed `JsonBranch` class and leverages the newly added `JsonPath.compile(path)` method.