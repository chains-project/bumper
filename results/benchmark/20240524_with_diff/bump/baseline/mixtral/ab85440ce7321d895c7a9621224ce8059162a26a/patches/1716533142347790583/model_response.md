Here's the fixed `isUploadStarted` method:

```java
private static ResponseMatcher isUploadStarted() {
    boolean startsWith = "/v2/test/blobs/uploads/".startsWith("/");
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            new StringStartsWith(startsWith, "/v2/test/blobs/uploads/")
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", new IsNot<>(Matchers.emptyString()))
    );
}
```

The issue was caused by the `StringStartsWith` constructor receiving two arguments of incompatible types. I've extracted the first argument into a separate variable `startsWith` and assigned the correct value to it.