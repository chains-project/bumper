```java
// TODO: review this AI generated patch!
@java.lang.Override
public com.artipie.http.Slice slice(final java.lang.String action) {
    return new com.artipie.http.Slice() {
        @java.lang.Override
        public com.artipie.http.Response response(final com.artipie.http.Request request, final com.artipie.http.Headers headers) {
            return new com.artipie.http.Response(
                new com.artipie.http.Status.Forbidden(),
                com.artipie.http.Headers.EMPTY,
                new java.io.ByteArrayInputStream("{\"error\":\"Unauthorized\"}".getBytes())
            );
        }
    };
}
```