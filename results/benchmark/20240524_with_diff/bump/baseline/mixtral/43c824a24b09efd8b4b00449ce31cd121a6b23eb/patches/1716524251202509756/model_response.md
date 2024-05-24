Here's a patch that you can apply to the code in order to fix the error:

```java
import de.gwdg.metadataqa.api.json.DataElement;

private static String extractFirst(JsonPathCache cache, DataElement branch) {
    List<String> list = extractList(cache, branch);
    if (!list.isEmpty())
      return list.get(0);
    return null;
  }

private static List<String> extractList(JsonPathCache cache, DataElement branch) {
    // Implementation to extract a list of strings from the DataElement
}
```

In the new library version, the `JsonBranch` class has been removed and replaced with the `DataElement` class. Therefore, we need to update the type of the `branch` parameter from `JsonBranch` to `DataElement` and modify the `extractList` method to accept a `DataElement` instead of a `JsonBranch`.