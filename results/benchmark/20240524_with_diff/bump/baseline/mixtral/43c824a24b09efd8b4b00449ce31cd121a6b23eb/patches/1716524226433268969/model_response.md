Here's the proposed patch:

```java
private static String extractFirst(JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement branch) {
  List<String> list = extractList(cache, branch);
  if (!list.isEmpty())
    return list.get(0);
  return null;
}

private static List<String> extractList(JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement branch) {
  // implementation depends on the context
}
```

The patch replaces the `JsonBranch` type with the new `DataElement` type, which is an addition in the new library version. Also, a new helper method `extractList` is introduced to encapsulate the logic of extracting a list from the `DataElement`. The implementation of this helper method depends on the specific context of the code.