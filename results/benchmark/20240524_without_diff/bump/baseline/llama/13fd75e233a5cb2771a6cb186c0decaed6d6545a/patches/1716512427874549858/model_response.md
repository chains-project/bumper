```java
private static ResponseMatcher isUploadStarted() {
    String prefix = "/v2/test/blobs/uploads/";
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            startsWith(prefix)
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", not(emptyString()))
    );
}
```