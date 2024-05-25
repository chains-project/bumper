Here's a proposed patch for the failing client code:

```java
import de.gwdg.metadataqa.api.json.JsonBranch;

// Add the following import statement
import de.gwdg.metadataqa.api.json.JsonPathUtils;

// Modify the following line
// JsonBranch branch = JsonPathUtils.getBranch(jsonNode, path);
JsonBranch branch = JsonPathUtils.getBranch(jsonNode, path, JsonBranch.class);
```

This patch imports the `JsonPathUtils` class and modifies the line that uses `getBranch` to include the class of the object being returned. This should fix the "cannot find symbol" error.