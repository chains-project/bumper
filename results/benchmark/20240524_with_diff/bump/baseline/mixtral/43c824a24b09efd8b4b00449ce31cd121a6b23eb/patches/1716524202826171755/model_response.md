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

The change is to replace `JsonBranch` with `DataElement` since the latter is the added equivalent in the new library version. Note that you'll also need to update the implementation of `extractList` accordingly.