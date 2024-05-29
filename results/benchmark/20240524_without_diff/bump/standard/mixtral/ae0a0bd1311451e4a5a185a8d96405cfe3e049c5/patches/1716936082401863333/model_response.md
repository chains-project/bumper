Here's the fixed version of the `isUploadStarted` method:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(
        com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.CoreMatchers.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", new org.hamcrest.CoreMatchers.StringStartsWith("0-0")),
        new com.artipie.http.hm.IsHeader("Content-Length", new org.hamcrest.CoreMatchers.IsEqual(0L)),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.CoreMatchers.IsInstanceOf(java.lang.String.class))
    );
}
```

Changes made:
- Replaced `org.hamcrest.core.StringStartsWith` with `org.hamcrest.CoreMatchers.StringStartsWith`.
- Replaced `org.hamcrest.core.IsEqual` with `org.hamcrest.CoreMatchers.IsEqual`.
- Added explicit cast to `0L` for `IsHeader("Content-Length", ...)`.

These changes should fix the error message related to the missing semicolon and ensure compatibility with the updated dependencies.