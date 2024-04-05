Here's a proposed patch for the failing method. It seems like the `JsonBranch` class is not being imported in the `MarcFactory` class. However, since I cannot modify the external dependency, I will modify the client code to accept a `String` representation of the `JsonBranch` instead.

```java
import de.gwdg.metadataqa.api.model.pathcache.JsonPathCache;
import java.util.List;
import java.util.StringJoiner;

private static String extractFirst(JsonPathCache cache, String branch) {
    List<String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}

private static List<String> extractList(JsonPathCache cache, String branch) {
    // Deserialize the 'branch' String into a JsonBranch object or use it directly, depending on the format
    // Then, use the deserialized object or 'branch' String to interact with the 'cache' object
    // ...
}
```

Note: You will need to update the `extractList` method in the `MarcFactory` class accordingly to handle the `String` representation of the `JsonBranch`.