Here's the updated `extractFirst` method that uses the new `DataElement` class instead of the removed `JsonBranch` class:

```java
private static String extractFirst(JsonPathCache cache, de.gwdg.metadataqa.api.json.DataElement branch) {
  List<String> list = extractList(cache, branch);
  if (!list.isEmpty())
    return list.get(0);
  return null;
}
```

This updated method should fix the error by using the new `DataElement` class instead of the removed `JsonBranch` class. Note that I replaced the type of the `branch` parameter from `JsonBranch` to `DataElement`.