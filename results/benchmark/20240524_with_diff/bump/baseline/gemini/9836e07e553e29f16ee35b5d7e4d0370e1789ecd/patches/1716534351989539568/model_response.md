```java
  // TODO: review this AI generated patch!
  private static ResponseMatcher isUploadStarted() {
    final String dockerUploadUUID = Matchers.not(Matchers.isEmptyString()).toString();
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            new StringStartsWith(false, "/v2/test/blobs/uploads/")
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", dockerUploadUUID)
    );
}
```