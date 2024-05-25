```java
private static ResponseMatcher isUploadStarted() {
    String startsWithPattern = "/v2/test/blobs/uploads/";
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            Matchers.startsWith(startsWithPattern)
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", Matchers.not(Matchers.isEmptyString()))
    );
}
```