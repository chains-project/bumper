Here's a possible patch for the `extractFirst` method, using the added `DataElement` class to replace the removed `JsonBranch` class:

```java
private static String extractFirst(JsonPathCache cache, DataElement branch) {
  List<String> list = extractList(cache, branch);
  if (!list.isEmpty())
    return list.get(0);
  return null;
}
```

This assumes that the `extractList` method can handle `DataElement` objects as well as `JsonBranch` objects. If not, you may need to modify `extractList` to handle `DataElement` objects appropriately.