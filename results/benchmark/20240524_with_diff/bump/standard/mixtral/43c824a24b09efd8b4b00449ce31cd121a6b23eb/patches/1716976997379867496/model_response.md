Here's the patched method with the updated import statement:

```java
import de.gwdg.metadataqa.api.json.DataElement;

private static String extractFirst(JsonPathCache cache, DataElement branch) {
    List<String> list = de.gwdg.metadataqa.marc.MarcFactory.extractList(cache, branch);
    if (!list.isEmpty())
        return list.get(0);

    return null;
}
```

The changes include:

1. Importing the `DataElement` class.
2. Replacing the `JsonBranch` type with `DataElement` in the method signature and local variables.