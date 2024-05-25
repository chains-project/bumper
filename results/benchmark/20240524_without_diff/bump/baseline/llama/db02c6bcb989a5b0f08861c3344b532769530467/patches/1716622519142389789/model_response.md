```java
private static ResponseMatcher isUploadStarted() {
    Pattern pattern = Pattern.compile("/v2/test/blobs/uploads/.*");
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            Matchers.matchesPattern(pattern)
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", Matchers.not(Matchers.emptyString()))
    );
}
```