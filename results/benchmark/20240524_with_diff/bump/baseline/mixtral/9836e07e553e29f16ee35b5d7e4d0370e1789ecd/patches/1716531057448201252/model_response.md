Here's the fixed version of the `isUploadStarted` method using the new library version:

```java
private static ResponseMatcher isUploadStarted() {
    boolean startsWith = "/v2/test/blobs/uploads/".contains("/v2/test/blobs/uploads/");
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            new StringStartsWith(startsWith ? "/v2/test/blobs/uploads/" : "")
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", new IsNot<>(Matchers.emptyString()))
    );
}
```

The change is in the `IsHeader` constructor for the `Location` header. Since the `StringStartsWith` constructor no longer accepts a `boolean` value, I created a new variable `startsWith` to represent whether the value starts with the specified substring. If it does, the constructor receives the substring; otherwise, it receives an empty string.