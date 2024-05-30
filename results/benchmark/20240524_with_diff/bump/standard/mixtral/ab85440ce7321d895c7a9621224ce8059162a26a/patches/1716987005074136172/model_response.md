Here's a possible patch for the code that should fix the error:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location", new org.hamcrest.core.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", "0-0"),
        new com.artipie.http.hm.IsHeader("Content-Length", "0"),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID", new org.hamcrest.core.IsNot.IsNotString(org.hamcrest.Matchers.emptyString()))
    );
}
```

The changes I made are:

* Replace `new org.hamcrest.core.StringStartsWith(false, "/v2/test/blobs/uploads/")` with `new org.hamcrest.core.StringStartsWith("/v2/test/blobs/uploads/")`. This is because the constructor of `StringStartsWith` now only takes a single argument, which is the expected prefix.
* Replace `new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString())` with `new org.hamcrest.core.IsNot.IsNotString(org.hamcrest.Matchers.emptyString())`. This is because `IsNot` no longer takes a `Matcher` argument directly, but instead takes an `IsNotString` instance that wraps the `Matcher`.