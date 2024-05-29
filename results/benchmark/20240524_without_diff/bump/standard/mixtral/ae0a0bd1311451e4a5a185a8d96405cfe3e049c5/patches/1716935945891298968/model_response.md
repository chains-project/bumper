Here's the fixed version of the `isUploadStarted` method:

```java
private static com.artipie.http.hm.ResponseMatcher isUploadStarted() {
    return new com.artipie.http.hm.ResponseMatcher(
        com.artipie.http.rs.RsStatus.ACCEPTED,
        new com.artipie.http.hm.IsHeader("Location",
            new org.hamcrest.core.StringStartsWith("/v2/test/blobs/uploads/")),
        new com.artipie.http.hm.IsHeader("Range", "0-0"),
        new com.artipie.http.hm.IsHeader("Content-Length", "0"),
        new com.artipie.http.hm.IsHeader("Docker-Upload-UUID",
            new org.hamcrest.Matcher<Object>(is(instanceOf(String.class))))
    );
}
```

The issue was caused by a missing `Matcher` constructor argument. I replaced

```java
new org.hamcrest.core.IsInstanceOf(java.lang.String.class)
```

with

```java
new org.hamcrest.Matcher<Object>(is(instanceOf(String.class)))
```

to fix the error.