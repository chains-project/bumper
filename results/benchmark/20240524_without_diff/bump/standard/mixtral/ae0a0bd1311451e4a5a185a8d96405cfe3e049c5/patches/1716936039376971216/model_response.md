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

Changes:

1. Replaced `new org.hamcrest.core.StringStartsWith` with `new org.hamcrest.CoreMatchers.StringStartsWith`
2. Replaced `new org.hamcrest.core.IsEqual` with `new org.hamcrest.CoreMatchers.IsEqual`
3. Added explicit type `0L` for `IsEqual` matcher
4. Wrapped each argument in a separate line for better readability