Here's the fixed version of the `isUploadStarted` method:

```java
private static ResponseMatcher isUploadStarted() {
    boolean startsWithSlash = "/v2/test/blobs/uploads/".charAt(0) == '/';
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            new StringStartsWith(startsWithSlash, "/v2/test/blobs/uploads/")
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", new IsNot<>(Matchers.emptyString()))
    );
}
```

The change is to extract the string prefix into a separate variable, and pass only the string to the `StringStartsWith` constructor. This way, the error caused by the change in the library version is resolved.