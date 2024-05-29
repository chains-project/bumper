Here's the fixed method with the issue resolved:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(
        com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.CoreMatchers.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", "0-0"),
        new com.artipie.http.hm.IsHeader("Content-Length", "0"),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsInstanceOf(java.lang.String.class))
    );
}
```

The issue was caused by an incorrect import of `StringStartsWith`. I replaced `org.hamcrest.core.StringStartsWith` with `org.hamcrest.CoreMatchers.StringStartsWith`.