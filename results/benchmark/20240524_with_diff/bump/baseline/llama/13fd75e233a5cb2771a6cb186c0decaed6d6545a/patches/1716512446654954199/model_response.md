```java
private static ResponseMatcher isUploadStarted() {
    String locationPrefix = "/v2/test/blobs/uploads/";
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            startsWith(locationPrefix)
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", not(isEmptyString()))
    );
}
```