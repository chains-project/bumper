Here is a fixed version of the code:

```java
@org.junit.jupiter.api.Test
void testScope() {
    final java.lang.String line = "GET /resource.txt HTTP/1.1";
    final java.lang.String action = "foo:bar:baz";
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> caction = new java.util.concurrent.atomic.AtomicReference<>();
    final java.util.concurrent.atomic.AtomicReference<java.lang.String> cline = new java.util.concurrent.atomic.AtomicReference<>();
    new com.artipie.docker.http.AuthScopeSlice(new com.artipie.docker.http.ScopeSlice() {
        @java.lang.Override
        public com.artipie.docker.http.Scope scope(final java.lang.String rqline) {
            cline.set(rqline);
            return new com.artipie.docker.http.Scope.FromString(action);
        }

        @java.lang.Override
        public com.artipie.http.Response response(final java.lang.String line, final java.lang.Iterable<java.util.Map.Entry<java.lang.String, java.lang.String>> headers, final org.reactivestreams.Publisher<java.nio.ByteBuffer> body) {
            return com.artipie.http.rs.StandardRs.OK;
        }
    }, ( headers, rline) -> java.util.concurrent.CompletableFuture.completedFuture(new com.artipie.http.auth.Authentication.SimpleUser("alice")), ( user, act) -> {
        caction.set(act);
        return true;
    }).response(line, com.artipie.http.Headers.EMPTY, com.artipie.asto.Content.EMPTY).send(( status, headers, body) -> java.util.concurrent.CompletableFuture.allOf()).toCompletableFuture().join();
    org.hamcrest.MatcherAssert.assertThat("Request line passed to slice", cline.get(), new org.hamcrest.core.IsEqual<>(line));
    org.hamcrest.MatcherAssert.assertThat("Scope passed as action to permissions", caction.get(), new org.hamcrest.core.IsEqual<>(action));
}
```

The change I made is to replace the anonymous class implementing `com.artipie.http.auth.Authentication` with a lambda expression that creates a `com.artipie.http.auth.Authentication.SimpleUser` object. The `SimpleUser` class is a concrete implementation of `com.artipie.http.auth.Authentication` that was added in a newer version of the library. This should fix the "cannot find symbol" error that you were seeing.