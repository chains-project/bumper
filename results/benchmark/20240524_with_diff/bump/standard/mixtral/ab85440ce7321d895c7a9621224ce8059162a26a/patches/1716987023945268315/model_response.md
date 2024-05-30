Here's a fixed version of the `isUploadStarted` method using the new library version:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", "0-0"),
        new com.artipie.http.hm.IsHeader("Content-Length", "0"),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot(org.hamcrest.CoreMatchers.emptyString()))
    );
}
```

The `StringStartsWith` constructor now requires only a single `String` argument, so I replaced the deprecated `StringStartsWith(boolean, String)` constructor with the new `StringStartsWith(String)` constructor. Similarly, I replaced the deprecated `IsNot(Matcher<T> matcher)` constructor with the new `IsNot(Matcher<T> matcher)` constructor from `CoreMatchers`.