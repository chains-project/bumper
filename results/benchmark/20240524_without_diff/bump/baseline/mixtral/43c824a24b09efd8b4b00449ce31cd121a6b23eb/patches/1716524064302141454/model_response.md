Here's the proposed patch to fix the error:

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

In the new library version, the `JsonBranch` class has been removed and replaced with `DataElement`. Therefore, we need to change the type of the `branch` parameter from `JsonBranch` to `DataElement` in both `extractFirst` and `extractList` methods.

Note that the implementation of `extractList` method depends on the context and is not provided here.