Here's a fixed version of the `isUploadStarted` method that should work with the new library version:

```java
private static ResponseMatcher isUploadStarted() {
    return new ResponseMatcher(
        RsStatus.ACCEPTED,
        new IsHeader(
            "Location",
            new StartsWith("/v2/test/blobs/uploads/")
        ),
        new IsHeader("Range", "0-0"),
        new IsHeader("Content-Length", "0"),
        new IsHeader("Docker-Upload-UUID", new Not(new StringDescription("", "")))
    );
}
```

The changes I made are:

* Replaced `new StringStartsWith(false, "/v2/test/blobs/uploads/")` with `new StartsWith("/v2/test/blobs/uploads/")`
* Replaced `Matchers.emptyString()` with `new StringDescription("", "")`

These changes use the new library methods `StartsWith` and `StringDescription` to replace the deprecated methods `StringStartsWith` and `emptyString()`.