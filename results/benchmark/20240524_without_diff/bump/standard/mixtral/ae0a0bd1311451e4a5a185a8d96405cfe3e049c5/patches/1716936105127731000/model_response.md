Here's the fixed `isUploadStarted` method:

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

The issue was caused by using `org.hamcrest.core` instead of `org.hamcrest.CoreMatchers`. I replaced the incorrect imports with the correct ones.