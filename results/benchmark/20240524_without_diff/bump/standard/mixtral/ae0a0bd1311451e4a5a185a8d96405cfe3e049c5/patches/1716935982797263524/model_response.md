Here's the updated `isUploadStarted` method with the required change:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(
        com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.CoreMatchers.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", "0-0"),
        new com.artipie.http.hm.IsHeader("Content-Length", "0"),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.CoreMatchers.IsInstanceOf(java.lang.String.class))
    );
}
```

The change is to replace `org.hamcrest.core` with `org.hamcrest.CoreMatchers` for the `StringStartsWith` and `IsInstanceOf` classes.