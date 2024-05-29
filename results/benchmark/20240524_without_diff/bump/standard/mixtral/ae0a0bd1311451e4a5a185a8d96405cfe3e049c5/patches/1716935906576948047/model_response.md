Here's a possible patch that should fix the error:
```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location",
            new org.hamcrest.core.StringStartsWith.StringStartsWith("/v2/test/blobs/uploads/")
        ),
        new com.artipie.http.hm.IsHeader("Range", "0-0"),
        new com.artipie.http.hm.IsHeader("Content-Length", "0"),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID",
            new org.hamcrest.core.IsNot.IsNot<>("")
        )
    );
}
```
The patch fixes the error by using the correct constructor for `StringStartsWith` which takes a single `String` argument. The `IsNot` matcher is also fixed to use the correct constructor that takes a single argument of type `T`.