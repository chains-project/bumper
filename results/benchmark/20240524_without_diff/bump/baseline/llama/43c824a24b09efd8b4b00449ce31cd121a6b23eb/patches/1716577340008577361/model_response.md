```java
private static String extractFirst(JsonPathCache cache, JsonBranch branch) {
    Object obj = cache.read(branch);
    if (obj instanceof List) {
        List<?> list = (List<?>) obj;
        if (!list.isEmpty())
            return list.get(0).toString();
    }
    return null;
}
```