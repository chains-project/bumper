Here's the fixed `isUploadStarted` method:

```java
private static ResponseMatcher isUploadStarted() {
    boolean startsWith = "/v2/test/blobs/uploads/".startsWith("/v2/test/blobs/uploads/");
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            new StringStartsWith(new IsEqual<String>(startsWith), "/v2/test/blobs/uploads/")
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", new IsNot<>(Matchers.emptyString()))
    );
}
```

The change is to extract the boolean value for the `StringStartsWith` constructor from the constant string, so that the constructor only receives a single argument.