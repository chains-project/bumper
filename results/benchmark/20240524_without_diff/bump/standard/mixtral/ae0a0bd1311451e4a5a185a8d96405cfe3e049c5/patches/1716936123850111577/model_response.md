Here's the fixed `isUploadStarted()` method:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(
        com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.CoreMatchers.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", new org.hamcrest.CoreMatchers.StringStartsWith("0-")),
        new com.artipie.http.hm.IsHeader("Content-Length", new org.hamcrest.CoreMatchers.IsEqual(0L)),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.CoreMatchers.IsInstanceOf(java.lang.String.class))
    );
}
```

Changes:

- Replace `org.hamcrest.core.StringStartsWith` with `org.hamcrest.CoreMatchers.StringStartsWith`
- Replace `org.hamcrest.core.IsEqual` with `org.hamcrest.CoreMatchers.IsEqual`
- Replace `new org.hamcrest.core.IsInstanceOf(java.lang.String.class)` with `org.hamcrest.CoreMatchers.IsInstanceOf(java.lang.String.class)`
- Replace `new com.artipie.http.hm.IsHeader("Range", "0-0")` with `new com.artipie.http.hm.IsHeader("Range", new org.hamcrest.CoreMatchers.StringStartsWith("0-"))`
- Replace `new com.artipie.http.hm.IsHeader("Content-Length", "0")` with `new com.artipie.http.hm.IsHeader("Content-Length", new org.hamcrest.CoreMatchers.IsEqual(0L))`