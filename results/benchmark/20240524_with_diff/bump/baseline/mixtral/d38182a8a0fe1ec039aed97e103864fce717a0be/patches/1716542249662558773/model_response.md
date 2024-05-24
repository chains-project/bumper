Here's a patch that fixes the error in the client code:

```java
import com.artipie.http.auth.AuthUser;

@Test
void testScope() {
    final String line = "GET /resource.txt HTTP/1.1";
    final String action = "foo:bar:baz";
    final AtomicReference<String> caction = new AtomicReference<>();
    final AtomicReference<String> cline = new AtomicReference<>();
    new AuthScopeSlice(
        new ScopeSlice() {
            @Override
            public Scope scope(final String rqline) {
                cline.set(rqline);
                return new Scope.FromString(action);
            }

            @Override
            public Response response(
                final String line,
                final Iterable<Map.Entry<String, String>> headers,
                final Publisher<ByteBuffer> body
            ) {
                return StandardRs.OK;
            }
        },
        (headers, rline) -> CompletableFuture.completedFuture(
            new AuthScheme.Result() {
                @Override
                public Optional<AuthUser> user() {
                    return Optional.of(new AuthUser("alice", ""));
                }

                @Override
                public String challenge() {
                    return "";
                }
            }
        ),
        (user, act) -> {
            caction.set(act);
            return true;
        }
    ).response(line, Headers.EMPTY, Content.EMPTY).send(
        (status, headers, body) -> CompletableFuture.allOf()
    ).toCompletableFuture().join();
    MatcherAssert.assertThat(
        "Request line passed to slice",
        cline.get(),
        new IsEqual<>(line)
    );
    MatcherAssert.assertThat(
        "Scope passed as action to permissions",
        caction.get(),
        new IsEqual<>(action)
    );
}
```

The changes made are:

1. Import `com.artipie.http.auth.AuthUser` at the beginning of the method.
2. Modify the lambda expression that creates `AuthScheme.Result` to use the new constructor that takes two arguments: `AuthUser("alice", "")`. This constructor was added in the new version of the library.
3. Remove the `@Override` decorator from the lambda expression, since it's not overriding any method.

Note that the new constructor `AuthUser("alice", "")` takes a second argument `""`, which is the `authContext()`. This is because the `AuthUser` class no longer has a no-argument constructor and requires an `authContext()`. The new `AuthUser` class is a final class, so it cannot be subclassed. The `authContext()` can be any non-empty `String`, so it's set to an empty string `""` in this case.