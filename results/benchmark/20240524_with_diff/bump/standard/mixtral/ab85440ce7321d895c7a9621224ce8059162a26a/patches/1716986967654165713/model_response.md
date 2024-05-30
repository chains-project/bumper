Here's a patch that you can apply to the failing client code:

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

The changes are:

* Replace `new org.hamcrest.core.StringStartsWith(false, "/v2/test/blobs/uploads/")` with `new org.hamcrest.core.StringStartsWith("/v2/test/blobs/uploads/")`.
* Replace `new org.hamcrest.core.IsNot<>(org.hamcrest.Matchers.emptyString())` with `org.hamcrest.CoreMatchers.emptyString()`.

The first change is necessary because the `StringStartsWith` constructor no longer accepts a `boolean` parameter in the new library version.

The second change is necessary because the `IsNot` constructor no longer accepts an instance of `Matchers` in the new library version. Instead, we can use `CoreMatchers` directly.