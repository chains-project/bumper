```java
// TODO: review this AI generated patch!
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
  return new com.artipie.http.async.AsyncSlice(
      future -> future.thenApply(
          response -> new com.artipie.http.async.AsyncResponse(
              response.status(),
              response.headers(),
              response.entity()
          )
      )
  );
}
```