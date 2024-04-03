Here's the fixed version of the `testScope` method using the new library version:

```java
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

The main change is the use of the new `AuthUser` class instead of the removed `Authentication.User` class. Also, the `AuthScheme.Result.user()` method now returns `Optional<AuthUser>` instead of `Optional<Authentication.User>`.