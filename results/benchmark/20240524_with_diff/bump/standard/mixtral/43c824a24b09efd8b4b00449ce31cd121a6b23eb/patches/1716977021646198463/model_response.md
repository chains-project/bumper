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

The change includes updating the `JsonBranch` type to `DataElement` in the method signature and the corresponding parameter. This is based on the added `DataElement` class in the new library version.