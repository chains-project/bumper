Here's the fixed version of the `isUploadStarted` method using the new library version:

```java
private static ResponseMatcher isUploadStarted() {
    boolean startsWith = "/v2/test/blobs/uploads/".contains("Location");
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader("Location", new StringStartsWith(startsWith)),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", new IsNot<>(Matchers.emptyString()))
    );
}
```

The change is in the `IsHeader` for the "Location" header. Instead of passing `new StringStartsWith(false, "/v2/test/blobs/uploads/")`, we first check if the string starts with the required substring and then pass the result to `StringStartsWith`. This way, the `StringStartsWith` constructor only receives a single argument.